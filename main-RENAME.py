import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
import pyotp
import robin_stocks.robinhood as robin

google = yf.Ticker("GOOG")

df = google.history(period="1d", interval="1m")
df = df[['Low']]
df['date'] = pd.to_datetime(df.index).time
df.set_index('date', inplace=True)
print(df.head())

X = df.index.values
Y = df['Low'].values

# The split point is the 10% of the dataframe length
offset = int(0.10*len(df))

X_train = X[:-offset]
Y_train = Y[:-offset]
X_test = X[-offset:]
Y_test = Y[-offset:]

plt.plot(range(0, len(Y_train)), Y_train, label="Train")
plt.plot(range(len(Y_train), len(Y)), Y_test, label="Test")
plt.legend()
plt.show()

model = ARIMA(Y_train, order=(5, 0, 1)).fit()
forecast = model.forecast(steps=1)[0]

print(f'Real data for time 0: {Y_train[len(Y_train) - 1]}')
print(f'Real data for time 1: {Y_test[0]}')
print(f'Predict data for time 1: {forecast}')

RH_USER_EMAIL = input("Email: ")
RH_PASSWORD = input('Password: ')
RH_MFA_CODE = "HRZSQZ2EEMFBKCM6"

timed_otp = pyotp.TOTP(RH_MFA_CODE).now()
login = robin.login(RH_USER_EMAIL, RH_PASSWORD, mfa_code=timed_otp)
print('current opt: ', timed_otp)

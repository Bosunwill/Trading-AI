import numpy as np
import pandas as pd

import tensorflow as tf

from tensorflow import feature_column
from tensorflow import keras
from tensorflow.keras import layers

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

import matplotlib.pyplot as plt
from matplotlib import rcParams

# Creates the dataframe for training
filename = 'DataSets\gain-loss_out.csv'
names = ['Date', 'Ticker', 'Open', 'High', 'Low', 'Close', 'Volume', 'Change', '50 Day MA', '100 Day MA', '200 Day MA','50 Day Support', '100 Day Support', '150 Day Support', '200 Day Support','50 Day Resistance', '100 Day Resistance', '150 Day Resistance', '200 Day Resistance','50 EMA', '100 EMA', '150 EMA', '200 EMA','50 AVG Gain', '100 AVG Gain', '150 AVG Gain', '200 AVG Gain','50 AVG Loss', '100 AVG Loss', '150 AVG Loss', '200 AVG Loss', 'RSI']
df = pd.read_csv(filename, names=names)

dates = df.pop('Date')
tickers = df.pop('Ticker')
Open = df.pop('Open')
High = df.pop('High')
Low = df.pop('Low')
Close = df.pop('Close')
Volume = df.pop('Volume')

# Check for empty columns
df = df.dropna()
print(df.isna().sum())

# df.iloc[:10]

# Split Data Set
X = df.drop('Change', axis=1)
y = df['Change']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.95, random_state=42)

print(X_train,y_train)

# Scale Data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Print Dot
class PrintDot(keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs):
        if epoch % 100 == 0: print('')
        print('.', end='')

# Train Model
tf.random.set_seed(42)
model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(256, activation='relu'),
    tf.keras.layers.Dense(256, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(
    loss=tf.keras.losses.binary_crossentropy,
    optimizer=tf.keras.optimizers.SGD(learning_rate=0.03),
    metrics=[
        tf.keras.metrics.BinaryAccuracy(name='accuracy'),
        tf.keras.metrics.Precision(name='precision'),
        tf.keras.metrics.Recall(name='recall')
    ]
)

early_stop = keras.callbacks.EarlyStopping(monitor='val_loss', patience=10)

model.fit(X_train_scaled, y_train, epochs=1, callbacks=[early_stop, PrintDot()])


model.save('saved_model/stockTFGainLossModel.h5')


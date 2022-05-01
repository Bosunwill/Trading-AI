from __future__ import absolute_import, division, print_function

import pathlib

import pandas as pd
import seaborn as sns
import numpy as np

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

import matplotlib.pyplot as plt


# Creates the dataframe for training
filename = 'DataSets\out.csv'
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
print(df.isna().sum())

train_dataset = df.sample(frac=0.8, random_state=32)
test_dataset = df.drop(train_dataset.index)

# Examine Data
# sns.pairplot(train_dataset[['Change', '50 Day MA','50 Day Support','50 Day Resistance','50 EMA','50 AVG Gain','50 AVG Loss','RSI']], diag_kind = 'kde')
# plt.show()

train_stats = train_dataset.describe()
train_stats.pop('Change')
train_stats = train_stats.transpose()
print(train_stats)

# Seperate Labels
train_labels = train_dataset.pop('Change')
test_labels = test_dataset.pop('Change')

# Normalize Data
def norm(x):
    return (x - train_stats['mean']) / train_stats['std']
normed_train_data = norm(train_dataset)
normed_test_data = norm(test_dataset)

# Build Model
def build_model():
    model = keras.Sequential([
        layers.Dense(1024, activation=tf.nn.relu, input_shape=[len(train_dataset.keys())]),
        layers.Dense(128, activation=tf.nn.relu),
        layers.Dense(1)
        ])
    optimizer = tf.keras.optimizers.RMSprop(0.001)
    model.compile(loss='mse', optimizer = optimizer, metrics = ['mean_absolute_error','mean_squared_error'])
    return model

model = build_model()

early_stop = keras.callbacks.EarlyStopping(monitor='val_loss', patience=10)

model.summary()

example_batch = normed_train_data[:10]
example_result = model.predict(example_batch)
print(example_result)

class PrintDot(keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs):
        if epoch % 100 == 0: print('')
        print('.', end='')

EPOCHS = 100

history = model.fit(
    normed_train_data, train_labels, epochs=EPOCHS, validation_split = 0.2, verbose=0, callbacks=[early_stop, PrintDot()])

hist = pd.DataFrame(history.history)
hist['epoch'] = history.epoch
hist.tail()

def plot_history(history):
    hist = pd.DataFrame(history.history)
    hist['epoch'] = history.epoch

    plt.figure()
    plt.xlabel('Epoch')
    plt.ylabel('Mean Abs Error [Change]')
    plt.plot(hist['epoch'], hist['mean_absolute_error'], label='Train Error')
    plt.plot(hist['epoch'], hist['val_mean_absolute_error'], label='Val Error')
    plt.legend()
    plt.ylim([0,5])

    plt.figure()
    plt.xlabel('Epoch')
    plt.ylabel('Mean Spuare Error [$Change^2$]')
    plt.plot(hist['epoch'], hist['mean_squared_error'], label='Train Error')
    plt.plot(hist['epoch'], hist['val_mean_squared_error'], label='Val Error')
    plt.legend()
    plt.ylim([0,20])
    plt.show()

plot_history(history)

loss, mae, mse = model.evaluate(normed_test_data, test_labels, verbose=0)
print("Testing set Mean Abs Error: ${:5.2f}".format(mae))



test_predictions = model.predict(normed_test_data).flatten()



'''

 ██       ██  ██   ██████   ██████    ████    ██  ██      ██████   ██    ██    ████    ██  ██   ██  ██   ██████   ██  ██
 ██       ██  ██   ██         ██     ██  ██   ███ ██      ██       ████████   ██  ██   ██  ██   ██  ██     ██     ███ ██
 ██       ██  ██   ██         ██     ██████   ██ ███      ██       ██    ██   ██████   ██  ██   ██  ██     ██     ██ ███
 ██████   ██████   ██████   ██████   ██  ██   ██  ██      ██████   ██    ██   ██  ██   ██████    ████    ██████   ██  ██

'''

from imp import get_magic
from pkgutil import get_data
from scipy.special import gamma
import matplotlib.pyplot as plt
import math
import csv
import keras
import tensorflow as tf
import keras.backend as K
from keras.utils.vis_utils import plot_model
import numpy as np

# Generates random data for the neural net to be trained and use as validation
DATA_SIZE = 5000000


def genData(min, max):
    x_ = (max-min) * np.random.rand(DATA_SIZE) + min
    y_ = sigmoid(gamma(x_ + 1), gamma(min + 1), gamma(max + 1))
    return x_, y_


def sigmoid(n, min, max):  # Non-Linear normilization, WHERE MIN MAX ARE ABSOLUTE MIN AND MAX ON THE INTERVAL
    var1 = 8/(max-min)
    var2 = n-((max+min)/2)
    return 1/(1+K.exp(-var1*var2))


# Inverse of sigmoid, WHERE MIN MAX ARE ABSOLUTE MIN AND MAX ON THE INTERVAL
def sigmoidInverse(n, min, max):
    return math.log((1/n)-1)/(-8/(max-min)) + (max+min)/2


# Neural Net
min = 0
max = 5


def func(x):
    return gamma(x+1)


x, y = genData(min, max)
x_test, y_test = genData(min, max)
model = keras.Sequential([
    keras.layers.Dense(8, input_shape=(1,)),
    keras.layers.Activation('elu'),
    keras.layers.Dense(1, activation='sigmoid'),
    keras.layers.Dense(1),
])

sgd = tf.keras.optimizers.SGD(0.01, momentum=0.9)
model.compile(optimizer=sgd, loss="mse")

history = model.fit(x=x, y=y, epochs=1, batch_size=64,
                    validation_data=(x_test, y_test))

model.save('model.h5')

reloaded = keras.models.load_model('model.h5')

print(sigmoidInverse(reloaded.predict([4.8]), func(min), func(max)))

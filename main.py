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
import keras.backend as K
import tensorflow as tf
import numpy as np


# Generates data for gamma function from n which is the maximum and step which is the step size, turns out this can be done a lot easier with nump. Also traning an Neural Net off of this data might be a bad idea due to how the inputs are not random.


def genGammaData(n, step, nameloc):
    if n > 170:
        raise ValueError("n must be less than 170")
    # Generates values for the x axis (inputs)
    values = [x*step for x in range(int(n/step))]
    nv = []
    for x in values:
        # fixes the fact that computers think .1 + .2 is 0.30000000000000004
        nv.append(round(x, abs(round(math.log(step, 10)))))
    with open(nameloc, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        for x in nv:
            # Writes the x and y values to the file, eventually this will be generalized to any function
            writer.writerow([str(x), str(gamma(x+1))])

# genGammaData(170, .0001, "data/gamma_0-170_E4.csv")
# genGammaData(170, .00001, "data/gamma_0-170_E5.csv")
# genGammaData(170, .000001, "data/gamma_0-170_E6.csv")


# Generates random data for the neural net to be trained and use as validation
DATA_SIZE = 5000000


def genData(min, max):
    x_ = (max-min) * np.random.rand(DATA_SIZE) + min
    y_ = sigmoid(gamma(x_ + 1), gamma(min + 1), gamma(max + 1))
    return x_, y_

# Turns out both the sigmoid function and normalize function are both built into keras so these are pointless but I am going to leave them since I made them and the are essential to understand what is happening

# These two functions are causing problems, although it still works pretty well


def sigmoid(n, min, max):  # Non-Linear normilization,  activation function (idk what that means yet but its gonna need to be changed later to be more accurate) ERROR - there is some inacuraccy in this functon thats causing some problems. I am pretty sure this is why I'm not getting too acurate of results.
    var1 = 8/(max-min)
    var2 = n-((max+min)/2)
    return 1/(1+K.exp(-var1*var2))


def sigmoidInverse(n, min, max):  # Inverse of sigmoid
    return math.log((1/n)-1)/(-8/(max-min)) + (max+min)/2


def normalize(n, min, max):  # Linear normilization
    return (n-min)/(max-min)


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
model.compile(optimizer=sgd, loss="mse", metrics=['accuracy'])

history = model.fit(x=x, y=y, epochs=3, batch_size=64,
                    validation_data=(x_test, y_test))

model.save('model.h5')

reloaded = keras.models.load_model('model.h5')

print(sigmoidInverse(reloaded.predict([4.8]), func(min), func(max)))

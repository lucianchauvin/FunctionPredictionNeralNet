'''

 ██       ██  ██   ██████   ██████    ████    ██  ██      ██████   ██    ██    ████    ██  ██   ██  ██   ██████   ██  ██
 ██       ██  ██   ██         ██     ██  ██   ███ ██      ██       ████████   ██  ██   ██  ██   ██  ██     ██     ███ ██
 ██       ██  ██   ██         ██     ██████   ██ ███      ██       ██    ██   ██████   ██  ██   ██  ██     ██     ██ ███
 ██████   ██████   ██████   ██████   ██  ██   ██  ██      ██████   ██    ██   ██  ██   ██████    ████    ██████   ██  ██

'''

from scipy.special import gamma
import matplotlib.pyplot as plt
import math
import csv


# Generates data for gamma function from n which is the maximum and step which is the step size
def genGammaData(n, step, nameloc):
    if n > 170:
        raise ValueError("n must be less than 170")
    # Generates values for the x axis (inputs)
    values = [x*step for x in range(int(n/step))]
    nv = []
    for x in values:
        # fixes the fact that computers think .1 + .2 is .3000000000000000004
        nv.append(round(x, abs(round(math.log(step, 10)))))
    with open(nameloc, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        for x in nv:
            # Writes the x and y values to the file, eventually this will be generalized to any function
            writer.writerow([str(x), str(gamma(x+1))])


# genGammaData(170, .0001, "data/gamma_0-170_E4.csv")
# genGammaData(170, .00001, "data/gamma_0-170_E5.csv")
# genGammaData(170, .000001, "data/gamma_0-170_E6.csv")

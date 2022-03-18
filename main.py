'''

 ██       ██  ██   ██████   ██████    ████    ██  ██      ██████   ██    ██    ████    ██  ██   ██  ██   ██████   ██  ██
 ██       ██  ██   ██         ██     ██  ██   ███ ██      ██       ████████   ██  ██   ██  ██   ██  ██     ██     ███ ██
 ██       ██  ██   ██         ██     ██████   ██ ███      ██       ██    ██   ██████   ██  ██   ██  ██     ██     ██ ███
 ██████   ██████   ██████   ██████   ██  ██   ██  ██      ██████   ██    ██   ██  ██   ██████    ████    ██████   ██  ██

'''

from scipy.special import gamma
import math


def genData(n, step):
    if n > 170:
        raise ValueError("n must be less than 170")
    values = [x*step for x in range(int(n/step))]
    nv = []
    for x in values:
        nv.append(round(x, abs(round(math.log(step, 10)))))
    with open('gamma_0-170_E5.txt', 'w') as f:
        for x in nv:
            f.write(str(x) + ' ' + str(gamma(x+1)) + "\n")


genData(170, .00001)

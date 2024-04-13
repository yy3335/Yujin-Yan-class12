import numpy as np

def FizzBuzz(start, finish):
    numvec = np.arange(start, finish + 1)
    objvec = np.empty(numvec.shape, dtype=object)
    objvec[:] = numvec
    objvec[(numvec % 3 == 0) & (numvec % 5 != 0)] = 'fizz'
    objvec[(numvec % 5 == 0) & (numvec % 3 != 0)] = 'buzz'
    objvec[(numvec % 3 == 0) & (numvec % 5 == 0)] = 'fizzbuzz'
    return objvec.tolist()
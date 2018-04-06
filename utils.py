import numpy as np

def stateNameToCoords(name):
    return [int(name.split('x')[1].split('y')[0]), int(name.split('x')[1].split('y')[1])]

def normalize(v):
    s = np.linalg.norm(v)
    if s == 0:
        return v
    else:
        return v/s

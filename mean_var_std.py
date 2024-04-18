import numpy as np

def calculate(list):
    #step 1: throw an error
    if len(list) != 9:
        raise ValueError('List must contain nine numbers')

    a = np.array(list).reshape((3, 3))
    #a = np.array([list[:3], list[3:6], list[6:]], dtype=np.int)    
    calculations = {
        'mean': [a.mean(axis=0), a.mean(axis=1), a.mean()],
        'variance': [a.var(axis=0), a.var(axis=1), a.var()],
        'standard deviation': [a.std(axis=0), a.std(axis=1), a.std()],
        'max': [a.max(axis=0), a.max(axis=1), a.max()],
        'min': [a.min(axis=0), a.min(axis=1), a.min()],
        'sum': [a.sum(axis=0), a.sum(axis=1), a.sum()]
    }

    return calculations
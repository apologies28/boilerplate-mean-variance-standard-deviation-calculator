import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    arr1 = np.array(list).reshape(3, 3)
    calculations = {
        "mean": [arr1.mean(axis=i).tolist() for i in [0, 1, None]],
        "variance": [arr1.var(axis=i).tolist() for i in [0, 1, None]],
        "standard deviation": [arr1.std(axis=i).tolist() for i in [0, 1, None]],
        "max": [arr1.max(axis=i).tolist() for i in [0, 1, None]],
        "min": [arr1.min(axis=i).tolist() for i in [0, 1, None]],
        "sum": [arr1.sum(axis=i).tolist() for i in [0, 1, None]],
    }

    return calculations
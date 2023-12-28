import numpy as np


def calculate(list):
  if len(list) != 9:
    list = list.fillana(0)
  else:
    a = np.array(list).reshape(3, 3)
    mean = [[a.mean(axis=0)], [a.mean(axis=1)],np.mean(a) ]
    variance = [[a.var(axis=0)], [a.var(axis=1)],np.var(a)]
    sd = [[a.std(axis=0)], [a.std(axis=1)], np.std(a)]
    max = [[a.max(axis=0)], [a.max(axis=1)], np.max(a)]
    min = [[a.min(axis=0)], [a.min(axis=1)], np.min(a)]
    sum = [[a.sum(axis=0)], [a.sum(axis=1)], np.sum(a)]
    calculations = {
        "mean": mean,
        "variance": variance,
        "standard deviation": sd,
        "max": max,
        "min": min,
        "sum": sum
    }     
    return calculations

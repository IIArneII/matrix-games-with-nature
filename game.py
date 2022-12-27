import numpy as np


def max_min_criterion(a: np.ndarray):
    m = a.min(axis=1)
    return m, np.argmax(m)

def max_max_criterion(a: np.ndarray):
    m = a.max(axis=1)
    return m, np.argmax(m)

def hurwitz_criterion(a: np.ndarray, p: float = 0.5):
    m = np.array(list(map(lambda x: p * max(x) + (1 - p) * min(x), a)))
    return m, np.argmax(m)

def bayes_criterion(a: np.ndarray, p: np.ndarray):
    m = np.array(list(map(lambda x: sum(x * p), a)))
    return m, np.argmax(m)

def laplace_criterion(a: np.ndarray):
    m = np.array(list(map(lambda x: sum(x) / len(x), a)))
    return m, np.argmax(m)

def savage_criterion(a: np.ndarray):
    m = (a.max(axis=0) - a).max(axis=1)
    return m, np.argmin(m)

import numpy as np

def t_norm_min(a, b):
    return np.minimum(a, b)  # Minimum

def t_norm_product(a, b):
    return a * b  # Iloczyn

def t_norm_lukasiewicz(a, b):
    return np.maximum(0, a + b - 1)  # Łukasiewicz




def t_conorm_max(a, b):
    return np.maximum(a, b)  # Maksimum

def t_conorm_probabilistic_sum(a, b):
    return a + b - a * b  # Suma probabilistyczna

def t_conorm_lukasiewicz(a, b):
    return np.minimum(1, a + b)  # Łukasiewicz
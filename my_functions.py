import numpy as np


def gaussian(t, sig_t):
    return np.exp(-(t ** 2) / (2 * sig_t ** 2))


def shifted_gaussian(t, sig_t):
    return np.exp(-((t - 1) ** 2) / (2 * sig_t ** 2))


def rect(t, width=3):
    return np.abs(t) < width / 2


def cosine(t, freq=1):
    return np.sin(2 * np.pi * freq * t)


def modulated_gaussian(t, freq=5):
    freq = 5
    x = np.exp(-(t ** 2) / (2 * 0.1 ** 2)) * np.cos(2 * np.pi * freq * t)


def beat_signal(t, freq1=2, freq2=4):
    freq1 = 2
    freq2 = 4
    return (np.cos(2 * np.pi * freq1 * t) + np.sin(2 * np.pi * freq2 * t)) * np.exp(
        -(t ** 2) / (2 * 1 ** 2)
    )

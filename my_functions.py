import numpy as np

def get_vars(x, N, dt):
    # note the fftshift - placing the zero of frequency in the middle for
    # numerical FFT
    # note normalization by factor dt - parsavel
    u = np.fft.fftshift(np.fft.fft(np.fft.ifftshift(x))) * dt
    # create frequency vector - with odd/even disambiguation similar to time vector
    if N % 2 == 0:
        f = np.arange(-1, (1 + 1 / N), (2 / N))[1:] * 1 / (2 * dt)
    else:
        f = np.arange(-(N - 1) / 2, (N + 1) / 2, 1) / (N * dt)
    df = f[1] - f[0]
    # inverse transform (note normalization by 1/dt - parsavel)
    x2 = np.fft.fftshift(np.fft.ifft(np.fft.ifftshift(u))) / dt
    return u, f, x2

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

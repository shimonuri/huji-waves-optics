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


def get_t(N):
    if N % 2 == 0:
        t = np.arange(-N / 2, N / 2, 1) * dt
    else:
        t = np.arange(-(N - 1) / 2, N / 2, 1) * dt

    return t

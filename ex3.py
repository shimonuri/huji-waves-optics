import numpy as np
import matplotlib.pyplot as plt
import my_functions
import utils

dt = 0.003
N = 2 ** 11
omega = 2 * np.pi


t = utils.get_t(N, dt)

x = my_functions.cosine(t)


u, f, x2 = utils.get_vars(x, N, dt)

fig, ax = plt.subplots(1, 2)
ax[0].plot(f, np.abs(u), label="Absolute Value", linestyle="solid", linewidth=2)
ax[0].plot(f, np.abs(u), label="Absolute Value", linestyle="solid", linewidth=2)
ax[0].plot(f, np.real(u), label="Real", linestyle="dotted", linewidth=3, color="black")
ax[0].plot(f, np.imag(u), label="Imaginary", linewidth=2)
ax[0].set_xlim(-10, 10)
ax[0].grid()
ax[0].legend(loc="upper left")
ax[0].set_title("Frequency space")
ax[0].set_xlabel("Frequency")

ax[1].plot(t, x, label="Original", linewidth=2)
ax[1].plot(
    t, np.real(x2), label="Inverse", linestyle="dotted", linewidth=3, color="black"
)
ax[1].set_xlim(-5, 5)
ax[1].legend()
ax[1].grid()
ax[1].set_title("Temporal space")
ax[1].set_xlabel("Time")

plt.show()

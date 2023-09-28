import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft,ifft
from scipy.signal import tf2zpk, freqz, lfilter

def PoleZeroPlot(b, a):
    (zeros,poles,gain) = tf2zpk(b, a)
    angle = np.linspace(-np.pi,np.pi,50)
    cirx = np.sin(angle)
    ciry = np.cos(angle)
    plt.figure()
    plt.plot(poles.real, poles.imag, 'x', zeros.real, zeros.imag, 'o', cirx,ciry, 'k-')
    plt.grid()

    plt.xlim((-1.5, 1.5))
    plt.xlabel('Real')
    plt.ylim((-1.5, 1.5))
    plt.ylabel('Imag')
    plt.gcf().set_figwidth(5)
    return (zeros,poles,gain)
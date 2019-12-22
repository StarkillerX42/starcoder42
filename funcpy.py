"""A number of functions that don't come from physics or astronomy"""

import sys
import numpy as np
from .physics import planck, estimate_rgb


def random_colors(n=1, red=1.0, green=0.5, blue=0.3):
    """Produces a random [re, gr, bl] color with the given maxes of red, green,
    and blue. The default values are meant to mimic a globular cluster.

    Inputs:
    N: Number of [re, gr, bl] arrays given in the output as a list.
    green: The amount of green in the result. Bigger number gives more green
    blue: The amount of blue in teh result. Bigger number gives more blue.

    Returns:
    A [] list of [re, gr, bl] arrays of length N, default 1 output."""
    colors = []
    for i in range(n):
        re = np.random.random() * red + red
        gr = np.random.random() * green + green
        bl = np.random.random() * blue + blue
        biggest = np.max([re, gr, bl])
        re = re / biggest
        gr = gr / biggest
        bl = bl / biggest
        colors.append([re, gr, bl])
    return colors


def wavelength_to_rgb(wavelength, gamma=1.0):
    """This converts a given wavelength of light to an
    approximate RGB color value. The wavelength must be given
    in nanometers in the range from 380 nm through 750 nm
    (789 THz through 400 THz).
    Based on code by Dan Bruton
    http://www.physics.sfasu.edu/astro/color/spectra.html
    """

    wavelength = float(wavelength)
    if 380 <= wavelength <= 440:
        attenuation = 0.3 + 0.7 * (wavelength - 380) / (440 - 380)
        re = ((-(wavelength - 440) / (440 - 380)) * attenuation) ** gamma
        gr = 0.0
        bl = (1.0 * attenuation) ** gamma
    elif 440 <= wavelength <= 490:
        re = 0.0
        gr = ((wavelength - 440) / (490 - 440)) ** gamma
        bl = 1.0
    elif 490 <= wavelength <= 510:
        re = 0.0
        gr = 1.0
        bl = (-(wavelength - 510) / (510 - 490)) ** gamma
    elif 510 <= wavelength <= 580:
        re = ((wavelength - 510) / (580 - 510)) ** gamma
        gr = 1.0
        bl = 0.0
    elif 580 <= wavelength <= 645:
        re = 1.0
        gr = (-(wavelength - 645) / (645 - 580)) ** gamma
        bl = 0.0
    elif 645 <= wavelength <= 750:
        attenuation = 0.3 + 0.7 * (750 - wavelength) / (750 - 645)
        re = (1.0 * attenuation) ** gamma
        gr = 0.0
        bl = 0.0
    else:
        re = 0.0
        gr = 0.0
        bl = 0.0
    return [int(re), int(gr), int(bl)]


def blackbody_color(temp=5800):
    """Returns the color of a blackbody of temperature t
    :param temp: A temperature in Kelvin or array of temperatures in kelvin
    :return: An array of shape len(temp)x3 of rgb colors"""
    wavelengths = np.linspace(400, 700, 250)
    if isinstance(temp, (float, int)):
        fluxes = planck(wavelengths, temp=temp)
        color = estimate_rgb(wavelengths, fluxes)
    elif isinstance(temp, (list, np.ndarray)):
        color = []
        for i, t in enumerate(temp):
            fluxes = planck(wavelengths, temp=t)
            color.append(estimate_rgb(wavelengths, fluxes))
        color = np.array(color)
    else:
        raise TypeError("Inputs must be given as an int, float, list, or array")
    return color


def random_decay_simulation(n, true_half_life):
    """Gives the time it takes for a set of N particles to decay. This is a
    simulation code, so its output will be extremel variable, espeically when
    N is small. Run this simulation many times to establish a reliable expected
    value.

    Inputs:
    N: The number of particles in the simulation
    true_half_life: Expected halflife of the partcle. In any units of time.

    Returns:
    The time of which the half of the particles have decayed in this particular
    simulation. This number will be different every time this is run. Returns
    the same units as given in input.
    """

    scale = true_half_life / np.log(2)
    time_decay = np.random.exponential(scale, n)
    half_decay = np.percentile(time_decay, 50)
    return half_decay


def find_index(array, val, print_it=False):
    bool_arr = array < val
    ind = np.where(bool_arr)[0][0]
    if print_it:
        print("First index found: {}".format(ind))
    return ind


def describe(a, print_it=False):
    """Summarize the basic characteristics of an array."""
    print("Data type is {}".format(type(a)))
    a = np.array(a)
    print("Size is {}".format(a.size))
    print("Shape is {}".format(a.shape))
    print("Number of dimensions is {}".format(a.ndim))
    try:
        print("Maximum value is {}".format(a.max()))
        print("Minimum value is {}".format(a.min()))
        print("Mean value is {}".format(a.mean()))
        print("Standard Deviation is {}".format(a.std()))
    except AttributeError:
        print("Array contains values which are not ints or floats")
    if print_it:
        print("Contents are...\n{}".format(a))
 

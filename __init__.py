"""This is my own code library. It has many cool functions using the numpy and
sympy libraries. Everything tries to be in snake_case, but dictionary keys are
still in CapitalCase. For more extensions on this involving sympy, try
starcoder42.math. It's recommended you import this via
import starcoder42 as s
import starcoder42.math
Some notable benefits of this is it automatically imports the function reload
available as s.reload. It also only imports sympy if you import
starcoder42.math which helps optimize code if sympy isn't in use.

Sections:
1. Constants
2. Conversion factors
3. Conversion functions
4. Math functions
5. Physics functions
6. Python functions


"""
import numpy as np
import sys

if sys.version_info.major == 3:
    from importlib import reload

__version__ = 3.6
__author__ = "Dylan Gatlin"

# 1. Constants
G = 6.674e-11  # N*m^2/kg^2
h = 6.6261e-34  # J*s
epsilon_0 = 8.854e-12  # F/m
mu_0 = 1.257e-6  # H/m
c = 2.99792e8  # m/s
sigma = 5.6704e-8  # W/m^2/K^4
hbar = 1.05457e-34  # J*s
k = 8.98755e9  # Nm^2/C^2
tau = 2 * np.pi
kb = 1.380648e-23
alphabet = "ABCDEFHGIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !?"

# 2. Conversion factors
# Masses
masses = {"Protons": 1.67262e-27,
          "Electrons": 9.10938e-31,
          "Neutrons": 1.67493e-27,
          "Suns": 1.98843e30,
          "Earths": 5.97220e24,
          "Jupiters": 1.89813e27,
          "Dylans": 70  # approximately
          }
massesAMU = {"CO2": 44,
             "MOxygen": 32,
             "MHydrogen": 2,
             "MNitrogen": 28,
             "Water": 18,
             "H2O": 18,
             "Methane": 16,
             "SulfurDioxide": 64,
             "MArgon": 40
             }
avrogadro = 6.02e23

# Charges
charges = {"Electron": -1.60218e-19,  # C
           "Proton": 1.60218e-19  # C
           }

heat_capacities = {"H2O": 4184.,
                   "Si": 712.}

densities = {"H2O": 1000.,
             "Si": 2650.}
# Distances
distances = {"AstronomicalUnits": 1.49598e11,
             "AU": 1.49598e11,
             "LightYears": 9.46e15,
             "Parsecs": 3.08568e16,
             "Kiloparsecs": 3.08568e19,
             "Megaparsecs": 3.08568e22,
             "Kilometers": 1000,
             "Nanometers": 1.e-9,
             "Microns": 1.e-6,
             "Angstroms": 1.e-10,
             "EarthRadii": 6.37101e6,
             "StellarRadii": 6.95700e8,
             "MoonRadii": 1.7375e6
             }

times = {"Minutes": 60.,
         "Hours": 3600.,
         "Days": 86400.,
         "Weeks": 604800.,
         "Years": 3.1536e7
         }

CGS = {"Gauss": 1.e-4,  # Teslas
       "Ergs": 1.e-7  # Joules
       }

evtoj = 1.60218e-19

# Angles
deg2as = 3600.
deg2am = 60.
deg2rad = np.pi / 180
rad2as = 206265.

# Absract Values
g = 9.807  # m/s^2
vesc = 11180.  # m/s


# 3. Unit Conversion Functions


def cel2kel(t):
    """Converts from Celsius to Kelvin"""
    return t + 274.2


def fahr2kel(t):
    """Converts an input temperature in fahrenheit to kelvins.
    Inputs:
    t: temperature, in Fahrenheit

    Returns:
    Temperature, in kelvins
    """
    return (t + 459.67) * 5.0 / 9.0


def fahr2cel(t):
    """Converts an input temperature in fahrenheit to degrees celsius
    Inputs:
    t: temperature, in degrees Fahrenheit

    Returns:
    Temperature, in C
    """
    return (t - 32) * 5 / 9


def wavenum2wavelen(v):
    """converts from wavenumber in cm^-1 to wavelengths in nm"""
    return 1 / v * 1.0e7


def wavelen2wavenum(l):
    """Converts from wavelength in nm to wavenumber in cm^-1"""
    return 1 / l * 1.0e7


# 4. Math Functions


def mag(a):
    """This is a simple function to find the magnitude of any vector.

    :param a: (array or list) The list to be calculated for magnitude.
    1D, any length
    :return: Magnitude of a
    """
    a = np.array(a)
    magnitude = np.sqrt(np.sum(a ** 2))
    return magnitude


def unit(a):
    """This is a function dependent on mag(a) to create a unit Vector.
    :param a: (array) The input to be converted to a unit vector.
    1D, any length
    :return: A unit vector for a
    """
    unit_vector = a / mag(a)
    return unit_vector


# 5. Physics Functions


def force_gravity_mag(m1, m2, r):
    """Calculates the force magnitude between two particles m1 and m2 at a
    distance r according to Newton"s Law of gravitation, all units in SI.
    :param m1: (float) Mass of body 1
    :param m2: (float) Mass of body 2
    :param r: Distance between the 2 bodies
    :return: (float) The force of gravity between two points
    """
    force_mag = G * m1 * m2 / r ** 2
    return force_mag


def force_gravity(m1, m2, r1, r2):
    """Calculates the force vector between two particles m1 and m2 at r1 and r2
    according to Newton"s Law of gravitation, all units in SI.
    :param m1: (float) Mass of body 1
    :param m2: (float) Mass of body 2
    :param r1: (array) Position of particle 1
    :param r2: (array) Position of particle 2
    :return:
    """
    a = np.array(r1)
    b = np.array(r2)
    ab = b - a
    r = mag(ab)
    force_mag = force_gravity_mag(m1, m2, r)
    force_vec = force_mag * unit(ab)
    return force_vec


def force_electric_mag(q1, q2, r):
    """Calculates the force magnitude between two particles q1 and q2 at a
    distance r according to Coulomb"s Law, all units in SI.
    :param q1: (float) Charge of body 1
    :param q2: (float) Charge of body 2
    :param r: Distance between the 2 bodies
    :return: (float) The electrostatic force between two points
    """
    force_mag = k * q1 * q2 / r ** 2
    return force_mag


def force_electrostatic(q1, q2, r1, r2):
    """Calculates the force vector between two particles m1 and m2 at r1 and r2
    according to Newton"s Law of gravitation, all units in SI.
    :param q1: (float) Charge of body 1
    :param q2: (float) Charge of body 2
    :param r1: (array) Position of particle 1
    :param r2: (array) Position of particle 2
    :return: (array) A vector representing the electrostatic force between
    the two points.
    """
    a = np.array(r1)
    b = np.array(r2)
    ab = b - a
    r = mag(ab)
    force_mag = force_electric_mag(q1, q2, r)
    force_vec = force_mag * unit(ab)
    return force_vec


def stefan_boltzmann(t):
    """The Power per unit area of a blackbody. All units SI"""
    return sigma * t ** 4


def luminosity_star(r, t):
    """The luminosity of a star, derived from the Stefan-Boltzmann Law.
    All units SI"""
    return 4 * np.pi * r ** 2 * sigma * t ** 4


def wien(t):
    """The peak wavelength of a blackbody. Input in Kelvins, output in nm"""
    return 2.9e6 / t


def escape_velocity(m, r):
    """The escape velocity of an object at a distance r from a body with mass M.
    All units SI"""
    return np.sqrt(2 * G * m / r)


def planck(w, temp=5800):
    """Computes the Flux of a star at a given wavelength in W/m^2 Input
    wavelength is in nm Temperature is by default 5800, but can be set to any
    value as the second input

    Inputs:
    w: (float) The wavelength in nm
    Returns:
    brightness: (float) The planck function in units of W/m^3
    """
    assert temp != 0, "Temperature cannot be zero"
    temp = temp * 1.0
    w = w * 1e-9
    num = 2 * h * c ** 2
    den = w ** 5 * (np.exp(h * c / (w * kb * temp)) - 1)
    brightness = num / den
    return brightness


def integrate_spectrum(wavelengths, fluxes, w_lower, w_upper):
    """
    _this function performs a numerical integral of a spectrum
    using the trapezoid method.

    _arguments:
        wavelengths = a numpy array of wavelengths, in nm
        fluxes = a numpy array of fluxes corresponding to each wavelength
        w_lower = the lower wavelength limit of the integration
        w_upper = the upper wavelength limit of the integration

    _returns:
        the integral of the fluxes, from w_lower to w_upper
        (this should be one floating point number)
    """

    # select the subset of wavelengths and fluxes to include
    selection = (wavelengths >= w_lower) & (wavelengths <= w_upper)
    use_w = wavelengths[selection]
    use_flux = fluxes[selection]

    dh = (use_flux[:-1] + use_flux[1:]) / 2.
    dw = use_w[1:] - use_w[:-1]
    area = dh * dw

    return np.sum(area)


def estimate_rgb(wavelengths, fluxes):
    """
    This function estimates the rgb color of an object, from its spectrum.

    It calculates the integrals the flux over wavelength ranges that correspond
    roughly to the red, green, and blue colors displayed on computer monitors.

    Arguments:
        wavelengths = a numpy array of wavelengths, in nanometers
        fluxes = a numpy array of fluxes, corresponding to w

    Returns:
        an rgb color, expressed as a three-element array,
        with red as the first element, green the second, blue the third

        (In Python these values must span from 0.0 to 1.0, so you
        will need to renormalize your integrals by the maximum of
        the three values, to ensure this happens.)
    """
    assert np.all(fluxes >= 0), "Fluxes were not positive"
    re = integrate_spectrum(wavelengths, fluxes, 565, 660)
    gr = integrate_spectrum(wavelengths, fluxes, 485, 570)
    bl = integrate_spectrum(wavelengths, fluxes, 400, 490)
    # make an array
    rgb = np.array([re, gr, bl])
    # normalize by the maximum value
    biggest = np.max(rgb)
    rgb /= biggest
    assert all(rgb >= 0), "Something went wrong, rgb produced a negative value"
    assert all(rgb <= 1), "Something went wrong, rgb produce a value greater " \
                          "than one "

    return rgb


def lorentz(v):
    """Calculates the time dilation factor given a velocity as a factor of c.

    Inputs:
    v: A factor of the speed of light, units of "c"

    Output:
    a lorentz multiple, greater than 1, no units.
    """

    assert (np.abs(v) < 1)
    return 1 / np.sqrt(1 - v ** 2)


# 6. Python functions


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


if sys.version_info.major == 3:
    # Only for 3 because scope must be an int
    def iprint(x, scope: int=1, **kwargs):
        """This prints items indented by 4 spaces, to help clarify scope of
        operations. x is the value intended to be printed, scope is an integer
        of the number of indents desired.
        """
        print("", x, sep="    "*scope, **kwargs)

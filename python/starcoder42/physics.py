"""Functions that have physical meaning"""

# Local imports
from .constants import *


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


def net_force(masses, positions, algorithm):
    forces = []
    for i, pos in enumerate(positions):
        f = np.zeros(3)
        for j, posj in enumerate(positions):
            if i != j:
                f += algorithm(masses[i], masses[j], pos, posj)
        forces.append(f)
    forces = np.array(forces)
    return forces


def leapfrog(masses, ipositions, ivelocities, dt, algorithm):
    """Computes a leapfrog iteration"""

    iaccels = net_force(masses, ipositions, algorithm)
    v_half = ivelocities + iaccels * 0.5 * dt
    fpositions = ipositions + v_half * dt
    faccels = net_force(masses, fpositions, algorithm)
    fvelocities = v_half + faccels * 0.5 * dt

    return fpositions, fvelocities


def calculate_trajectories(masses, ipositions, ivelocities, t, dt, algorithm):
    """An n-body simulation calculated using algorithm function.

    Returns:
        Positions: An array of shape ntimes*nbodies*ndim
        Velocities: An array of the same shape
        Times: An array of times of shape ntimes
    """
    n_times = int(t/dt)
    times = np.linspace(0., t, n_times + 1)
    positions = [ipositions]
    velocities = [ivelocities]

    for i, time in enumerate(times):
        pos, vel = leapfrog(masses, positions[i], velocities[i], dt, algorithm)
        positions.append(pos)
        velocities.append(vel)

    positions = np.array(positions)
    velocities = np.array(velocities)

    return positions, velocities, times


def calculate_energy(masses, positions, velocities):
    u_tot = 0.
    for i, pos in enumerate(positions):
        for j, posj in enumerate(positions):
            if i != j:
                u_tot -= G * masses[i] * masses[j] / mag(pos-posj)
        u_tot += 0.5 * masses[i] * mag(velocities[i])**2

    return u_tot

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
    assert np.sum((wavelengths < 660) & (wavelengths > 400)) > 0, \
        "No wavelengths between 400 and 660"
    wavelengths = np.array(wavelengths)
    fluxes = np.array(fluxes)
    re = integrate_spectrum(wavelengths, fluxes, 565, 660)
    gr = integrate_spectrum(wavelengths, fluxes, 485, 570)
    bl = integrate_spectrum(wavelengths, fluxes, 400, 490)
    # make an array
    rgb = np.array([re, gr, bl])
    # print(rgb)
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


def mag(a):
    """This is a simple function to find the magnitude of any vector.

    :param a: (array or list) The list to be calculated for magnitude.
    1D, any length
    :return: Magnitude of a
    """
    a = np.array(a)
    magnitude = np.sqrt(np.sum(a**2))
    return magnitude


def unit(a):
    """This is a function dependent on mag(a) to create a unit Vector.
    :param a: (array) The input to be converted to a unit vector.
    1D, any length
    :return: A unit vector for a
    """
    unit_vector = a / mag(a)
    return unit_vector
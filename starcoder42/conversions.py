"""Conversion factors and conversion functions"""

import numpy as np

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


# Conversion Functions


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

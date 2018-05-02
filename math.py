import numpy as np
import sympy as sp
import sympy.abc
import sympy.matrices

r = sp.Rational
tau = 2 * sp.pi
cartesian = sp.symbols("x, y, z")
cylindrical = (sp.symbols("r"), sp.abc.phi, sp.symbols("z"))
spherical = (sp.symbols("r"), sp.abc.phi, sp.abc.theta)


def sec(x, **kwargs):
    """returns the secant of the angle x"""
    return 1 / np.cos(x, **kwargs)


def grad(f, space):
    """Returns the gradient of a vector field f given space defined as an
    array of sympy variables
    :param f: ND function
    :param space: (tuple,list) sympy symbols representing dimensions
    :return: ND gradient field
    """

    flist = []
    for i, var in enumerate(space):
        try:
            flist.append(f[i].diff(var))
        except (IndexError, TypeError):
            flist.append(f.diff(var))
    return sp.Array(flist)


def div(f, space):
    """Returns the divergence of a vector field f given space defined as an
    array of sympy variables
    :param f: ND function
    :param space: sympy symbols representing dimensions
    :return: divergence scalar"""
    assert len(f) == len(space), "Function and Variables Dimension must be " \
                                 "equal "

    flist = [fi.diff(v) for fi, v in zip(f, space)]
    return sum(flist)


def curl(f, space):
    """Returns the curl of a vector field f given space defined as an
    array of sympy variables
    :param f: 3D function
    :param space: (tuple,list) sympy symbols representing dimensions
    :return: 3D curl field"""
    assert len(f) == len(space) == 3, "curl only exists in 3D space"

    curls = [+f[2].diff(space[1]) - f[1].diff(space[2]),
             -f[2].diff(space[0]) + f[0].diff(space[2]),
             +f[1].diff(space[0]) - f[0].diff(space[1])]
    crl = sp.Array(curls)
    return crl


def laplacian(f, space):
    """Computes the laplacian of a vector function f given space defined as an
    array of sympy variables
    :param f: ND function or potential function
    :param space: ND array, tuple, function of sympy symbols defining the space
    :return: A sympy Mul object or possibly float
    """
    lap = 0
    try:
        for fd, var in zip(f, space):  # If it's a vector field
            lap += fd.diff(var)
    except (IndexError, AttributeError):  # If it's a scalar field
        for i, var in enumerate(space):
            lap += f.diff(var)
    return lap


def forward_derivative(f, x, dh):
    """
    Use the forward difference method to calculate the
    derivative of a function "f", evaluated at "x",
    using a step-size of "h"

    Inputs:
    f: A function of a variable x
    x: The point at which  to calculate the derivative
    h: step size, the smaller, the more precise

    Outputs:
    The derivative of f at x.
    """
    return (f(x + dh) - f(x)) / dh


def center_derivative(f, x, dh):
    """
    Use the central difference method to calculate the
    derivative of a function "f", evaluated at "x",
    using a step-size of "h" on both sides of the point f(x)

    Inputs:
    f: A function of a variable x
    x: The point at which  to calculate the derivative
    h: step size, the smaller, the more precise

    Outputs:
    The derivative of f at x.
    """
    return (f(x + dh) - f(x - dh)) / dh / 2.


def efoldingtime(times, values):
    """Assuming the array begins at an inital value, and converges before the
    end, this function finds the e-folding time of the array
    Inputs:
    times: (array) An array of times
    values: (array) An Array of values corresponding to the times in times
    Return:
    The amount of time it takes for this function to fold by e. This will return
    the first time where this occurs, and will only work if the values of values
    decay quasi-exponentially or exponentially."""
    assert len(times) == len(values)
    total_change = np.abs(values[0] - values[-1])
    fold = total_change / np.e
    boolean = np.abs(values - values[-1]) < fold
    fold_time = times[boolean][0]
    return fold_time


def jacobian(functions, space):
    """Calculates the jacobian of a sympy function, given space defined as an
    array of sympy variables
    Inputs:
    functions: (array) Continuous functions of ND
    space: (array) Variables of the functions

    Returns:
    The jacobian of a function, regardless of dimension    """
    mat = []
    for f in functions:
        dim = []
        for v in space:
            dim.append(f.diff(v))
        mat.append(dim)
    mat = sp.Matrix(mat)
    jac = mat.det()
    return jac.simplify()


def mag(a):
    """Computes the symbolic magnitude of a function. Unlike sc.mag, this
    function should be used in the conjunction of sympy and symbols

    :param a: (array or list) The list to be calculated for magnitude.
    1D, any length
    :return: Magnitude of a
    """
    a = np.array(a)
    magnitude = sp.sqrt(np.sum(a ** 2))
    return magnitude

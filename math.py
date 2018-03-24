import sympy as sp
import sympy.abc


def sec(x, **kwargs):
    """returns the secant of the angle x"""
    return 1 / np.cos(x, **kwargs)


def grad(f, variables):
    """Returns the gradient of a vector field f wrt. variables
    :param f: ND function
    :param varaibles: (tuple,list) sympy symbols representing dimensions
    :return: ND gradient field
    """

    flist = []
    for i, var in enumerate(variables):
        try:
            flist.append(f[i].diff(var))
        except (IndexError, TypeError):
            flist.append(f.diff(var))
    return sp.Array(flist)


def div(f, variables):
    """Returns the divergence of a vector field f wrt. variables

    :param f: ND function
    :param variables: sympy symbols representing dimensions
    :return: divergence scalar"""
    assert len(f) == len(variables), "Function and Variables Dimension must " \
                                     "be equal"

    flist = [fi.diff(v) for fi, v in zip(f, variables)]
    return sum(flist)


def curl(f, variables):
    """Returns the curl of a vector field f wrt. variables
    :param f: 3D function
    :param variables: (tuple,list) sympy symbols representing dimensions
    :return: 3D curl field"""
    assert len(f) == len(variables) == 3, "Function and variables dimension " \
                                          "be 3"

    curls = [+f[2].diff(variables[1]) - f[1].diff(variables[2]),
             -f[2].diff(variables[0]) + f[0].diff(variables[2]),
             +f[1].diff(variables[0]) - f[0].diff(variables[1])]
    curArr = sp.Array(curls)
    return curArr


def forwardDerivative(f, x, dh):
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


def centerDerivative(f, x, dh):
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


def eFoldingTime(timesArr, valArr):
    """Assuming the array begins at an inital value, and converges before the end,
    this function finds the e-folding time of the array
    Inputs:
    timesArr: (array) An array of times
    valArr: (array) An Array of values corresponding to the times in timesArr
    Return:
    The amount of time it takes for this function to fold by e. This will return
    the first time where this occurs, and will only work if the values of valArr
    decay quasi-exponentially or exponentially."""
    assert len(timesArr)==len(valArr)
    totalChange = np.abs(valArr[0] - valArr[-1])
    eFold = totalChange/np.e
    boolArr = np.abs(valArr-valArr[-1]) < eFold
    eFoldt = timesArr[boolArr][0]
    return eFoldt
from matrices import *


def place_into_focus(lense):
    if isinstance(lense, (Lense, ThinLense)):
        return lense*T(lense.F)
    else:
        raise TypeError("Wrong input parameter")

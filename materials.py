import math


def N(Y):
    A = 0.6961663
    B = 0.4079426
    C = 0.8974794
    D = 0.0684043
    E = 0.1162414
    F = 9.896161
    X1 = A*Y*Y/(Y*Y - D*D)
    X2 = B*Y*Y/(Y*Y - E*E)
    X3 = C*Y*Y/(Y*Y - F*F)

    return math.sqrt(1 + X1 + X2 + X3)


def N_BK7(Y):
    Y_ = Y*1e6
    A = 1.03961212
    B = 0.231792344
    C = 1.010469450
    D = 0.00600069867
    E = 0.0200179144
    F = 103.5606530
    X1 = A*Y_*Y_/(Y_*Y_ - D*D)
    X2 = B*Y_*Y_/(Y_*Y_ - E*E)
    X3 = C*Y_*Y_/(Y_*Y_ - F*F)

    return math.sqrt(1 + X1 + X2 + X3)
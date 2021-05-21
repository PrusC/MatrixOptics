import math


class Material(object):
    A = 1.0
    B = 1.0
    C = 1.0
    D = 1.0
    E = 1.0
    F = 1.0

    @classmethod
    def _get_wl_mkm(cls, wavelength):
        if wavelength <= 1e-5:
            return wavelength * 1e6
        elif 1e-5 < wavelength <= 10:
            return wavelength
        else:
            return wavelength * 1e-3

    @classmethod
    def n(cls, wavelength):
        x = cls._get_wl_mkm(wavelength)
        x1 = cls.A / (1 - cls.D / x**2)
        x2 = cls.B / (1 - cls.E / x**2)
        x3 = cls.C / (1 - cls.F / x**2)
        return math.sqrt(1 + x1 + x2 + x3)


class N_BK7(Material):
    A = 1.03961212
    B = 0.231792344
    C = 1.010469450
    D = 0.00600069867
    E = 0.0200179144
    F = 103.5606530


class FusedSilica(Material):
    A = 0.6961663
    B = 0.4079426
    C = 0.8974794
    D = 0.0684043 ** 2
    E = 0.1162414 ** 2
    F = 9.896161 ** 2


class N_SF5(Material):
    A = 1.52481889
    B = 0.187085527
    C = 1.42729015
    D = 0.011254756
    E = 0.0588995392
    F = 129.141675

# def N(Y):
#     A = 0.6961663
#     B = 0.4079426
#     C = 0.8974794
#     D = 0.0684043
#     E = 0.1162414
#     F = 9.896161
#     X1 = A*Y*Y/(Y*Y - D*D)
#     X2 = B*Y*Y/(Y*Y - E*E)
#     X3 = C*Y*Y/(Y*Y - F*F)
#
#     return math.sqrt(1 + X1 + X2 + X3)
#
#
# def N_BK7(Y):
#     Y_ = Y*1e6
#     A = 1.03961212
#     B = 0.231792344
#     C = 1.010469450
#     D = 0.00600069867
#     E = 0.0200179144
#     F = 103.5606530
#     X1 = A*Y_*Y_/(Y_*Y_ - D*D)
#     X2 = B*Y_*Y_/(Y_*Y_ - E*E)
#     X3 = C*Y_*Y_/(Y_*Y_ - F*F)
#
#     return math.sqrt(1 + X1 + X2 + X3)

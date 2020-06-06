import math


class GaussianBeam(object):

    def __init__(self, wl=1.064e-6, z=0.0, **kwargs):
        self._wl = wl
        self._z = z
        #  w=10e-6, R=float('inf'), q=None
        q = kwargs.get('q', None)
        if q is not None:
            self._q = None
        else:
            w = kwargs.get('w', 10e-6)
            R = kwargs.get('R', float('inf'))
            self._q = 1.0/R - (self._wl/(math.pi*w*w))*1j

    @property
    def wl(self):
        return self._wl

    @property
    def z(self):
        return self._z

    @property
    def q(self):
        return self._q

    @q.setter
    def q(self, value):
        if isinstance(value, complex):
            self._q = value
        else:
            raise ValueError("Wrong value: {}".format(value))

    @property
    def R(self):
        real = (1/self._q).real
        return 1/real if real != 0 else float('inf')

    @property
    def w(self):
        imag = -(1/self._q).imag
        if imag > 0:
            return math.sqrt(self._wl/(math.pi * imag))
        else:
            return float('inf')

    # @property
    # def zr(self):
    #     return

import math


class GaussianBeam(object):

    def __init__(self, wl=1.064e-6, **kwargs):
        if wl <= 1e-5:
            self._wl = wl
        elif 1e-5 < wl <= 10:
            self._wl = wl*1e-6
        else:
            self._wl = wl*1e-9
        # self._z = z
        q = kwargs.get('q', None)
        if q is not None:
            self._q = q
        else:
            w = kwargs.get('w', 10e-6)
            R = kwargs.get('R', float('inf'))
            self._q = 1.0/(1.0/R - (self._wl/(math.pi*w*w))*1j)

    @property
    def wavelength(self):
        return self._wl

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
        if real == 0:
            return float('inf')
        else:
            return 1/real

    @property
    def w(self):
        imag = -(1/self._q).imag
        if imag > 0:
            return math.sqrt(self._wl/(math.pi * imag))
        else:
            return float('inf')

    @property
    def waist(self):
        return math.sqrt(self.q.imag*self._wl/math.pi)

    @property
    def waist_position(self):
        return -self.q.real

    @property
    def rayleigh_length(self):
        return self.q.imag

    @property
    def z(self):
        return self.q.real

    def __str__(self):
        des = "/-------------------------------/\n"
        des += "Gaussian beam parameters:\n"
        des += "Q = {}\n".format(self.q)
        des += "w(z) = {} mkm\n".format(self.w*1e6)
        des += "R(z) = {}\n".format(self.R)
        des += "z = {} mm\n".format(self.z*1e3)
        des += "wavelength = {} nm\n".format(self.wavelength*1e9)
        des += "Rayleigh Length = {} mm\n".format(self.rayleigh_length*1e3)
        des += "waist = {} mkm\n".format(self.waist*1e6)
        des += "waist position = {} mm\n".format(self.waist_position*1e3)
        des += "/-------------------------------/\n"
        return des

    def Wz(self, z):
        d = (z-self.waist_position)/self.rayleigh_length
        return self.waist*math.sqrt(1 + d*d)

    def Rz(self, z):
        d = self.rayleigh_length/(z-self.waist_position)
        return (z-self.waist_position)*(1 + d*d)

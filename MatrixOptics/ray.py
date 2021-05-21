import numpy


class Ray(object):

    def __init__(self, y=0.0, alpha=0.0):
        self._y = float(y)
        self._alpha = float(alpha)

    @property
    def y(self):
        return self._y

    @property
    def alpha(self):
        return self._alpha

    @property
    def raw(self):
        return numpy.array([[self._y],
                            [self._alpha]])

    def __str__(self):
        des = 'Ray: y={}, alpha={}'.format(self._y, self._alpha)
        return des

    def __eq__(self, other):
        if isinstance(other, Ray):
            return False
        if self.y != other.y:
            return False
        if self.alpha != other.alpha:
            return False
        return True

import numpy
from ray import Ray
from gaussian import GaussianBeam


class ABCD(object):

    def __init__(self, *args):

        A, B, C, D = 1.0, 0.0, 0.0, 1.0
        if len(args) == 4:
            A, B, C, D = args[0], args[1], args[2], args[3]
            self._A = args[0]
            self._B = args[1]
            self._C = args[2]
            self._D = args[3]
        elif len(args) == 1 and isinstance(args[0], numpy.ndarray) and args[0].shape == (2, 2):
            mat = args[0]
            A = mat[0][0]
            B = mat[0][1]
            C = mat[1][0]
            D = mat[1][1]
        self._A = float(A)
        self._B = float(B)
        self._C = float(C)
        self._D = float(D)

    @property
    def A(self):
        return self._A

    @property
    def B(self):
        return self._B

    @property
    def C(self):
        return self._C

    @property
    def D(self):
        return self._D

    @property
    def matrix(self):
        return numpy.array([[self._A, self._B],
                            [self._C, self._D]])

    def __str__(self):
        return self.matrix.__str__()

    def __mul__(self, other):
        if isinstance(other, ABCD):
            return ABCD(self.matrix.dot(other.matrix))
            # return ABCD(numpy.dot(self.matrix, other.matrix))

        if isinstance(other, Ray):
            mat = self.matrix.dot(other.raw)
            return Ray(y=mat[0], alpha=mat[1])

        if isinstance(other, GaussianBeam):
            q2 = (self.A*other.q + self.B)/(self.C*other.q + self.D)
            return GaussianBeam(other.wavelength, q=q2)

    def __eq__(self, other):
        if not isinstance(other, ABCD):
            return False
        if self.A != other.A:
            return False
        if self.B != other.B:
            return False
        if self.C != other.C:
            return False
        if self.D != other.D:
            return False
        return True

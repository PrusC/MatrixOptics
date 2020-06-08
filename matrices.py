from abcd import ABCD


class SphericalRefractiveSurface(ABCD):

    def __init__(self, R, n2, n1=1.0):
        self._R = R
        self._n2 = n2
        self._n1 = n1
        A = 1
        B = 0
        C = float(-(n2-n1)/(n2*R))
        D = 1.0#float(n1/n2)
        super(SphericalRefractiveSurface, self).__init__(A, B, C, D)

    @property
    def R(self):
        return self._R


class Translation(ABCD):

    def __init__(self, d, n=1.0):
        super(Translation, self).__init__(1, float(d/n), 0, 1)


SRS = SphericalRefractiveSurface
T = Translation


class Lense(ABCD):

    def __init__(self, R1, R2, d, n, n_outer=1.0):
        L = SRS(R2, n, n_outer)*Translation(d, n)*SRS(R1, n_outer, n)
        super(Lense, self).__init__(L.matrix)

    @property
    def F(self):
        return -1.0/self.C


class ThinLense(ABCD):

    def __init__(self, f):
        super(ThinLense, self).__init__(1, 0, -1.0/f, 1)

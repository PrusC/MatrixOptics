from MatrixOptics.matrices import *
from MatrixOptics.gaussian import GaussianBeam
from MatrixOptics.materials import N_BK7

gauss = GaussianBeam(1064, w=7e-6)
print(gauss)

L = Lense(R1=25.84e-3, d=4.9e-3, n=N_BK7.n(gauss.wavelength))
print(L.F)
L2 = Lense(R1=9.87e-3, d=4e-3, n=N_BK7.n(gauss.wavelength))
print(L2.F)

gauss2 = L2*T(19.481e-3)*gauss
print(gauss2)

gauss3 = L2*T(19.481e-3)*GaussianBeam(1064, w=6.65e-6)
print(gauss3)

gauss4 = L2*T(19.481e-3)*GaussianBeam(1064, w=7.1e-6)
print(gauss4)

gauss5 = L*T(L.F)*gauss
print(gauss5)

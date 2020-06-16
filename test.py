from matrices import *
from gaussian import GaussianBeam
from materials import N_BK7

gauss = GaussianBeam(1064, w=7e-6)
print(gauss)

L = Lense(R1=25.84e-3, d=4.9e-3, n=N_BK7.n(gauss.wavelength))
print(L.F)
L2 = Lense(R1=9.87e-3, d=4e-3, n=N_BK7.n(gauss.wavelength))
# print(L2.F)
# gaus3 = L2*T(19.481e-3)*gaus
# print(gaus3)
#
# print('Left Spec')
# gaus3 = L2*T(19.481e-3)*GaussianBeam(1064, w=6.65e-6)
# print(gaus3)
#
# print('Right Spec\n')
# gaus3 = L2*T(19.481e-3)*GaussianBeam(1064, w=7.1e-6)
# print(gaus3)
#
# gaus3 = L*T(L.F)*GaussianBeam(1064, w=6.65e-6)

gaus3 = L*T(L.F)*gauss
print(gaus3)

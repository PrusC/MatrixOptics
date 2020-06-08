from matrices import *
from gaussian import GaussianBeam
# from ray import Ray
from materials import N_BK7

gaus = GaussianBeam(1064, w=7e-6)
print(gaus)

L = Lense(R1=25.84e-3, d=4.9e-3, n=N_BK7(gaus.wavelength))
L2 = Lense(R2=-9.87e-3, d=4e-3, n=N_BK7(gaus.wavelength))
print(L.F)
gaus3 = L*T(L.F)*gaus
print(gaus3)

gaus3 = L*T(70e-3)*gaus
print(gaus3)
gaus3 = L*T(24e-3)*gaus
# print(gaus3)


# gaus3=L2*T(10e-3)*L*T(19.46e-3)*gaus
# print(gaus3)

from matrices import *
from gaussian import GaussianBeam
from ray import Ray
from materials import N_BK7

gaus = GaussianBeam(1064, w=7e-6)
print(gaus)

L = Lense(float('inf'), -9.87e-3, 4e-3, N_BK7(gaus.wavelength), 1.0)
print(L.F)
gaus3 = L*T(L.F)*gaus
print(gaus3)

gaus3 = ThinLense(f=19.1e-3)*T(19.1e-3)*gaus
print(gaus3)



from matrices import *
from gaussian import GaussianBeam
from ray import Ray

gaus = GaussianBeam(1064, w=7e-6)
# gaus2 = T(20e-3, 1.0)*gaus
# print(gaus2)
gaus3 = ThinLense(f=20e-3)*T(20e-3)*gaus
print(gaus3)


gaus = GaussianBeam(1064, w=7e-6*1.1)
# gaus2 = T(20e-3, 1.0)*gaus
# print(gaus2)
gaus3 = ThinLense(f=20e-3)*T(20e-3, 1.0)*gaus
print(gaus3)

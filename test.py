from matrices import *
from gaussian import GaussianBeam
from ray import Ray

gaus = GaussianBeam(1064, w=7e-6)
gaus2 = T(20e-3, 1.0)*gaus
# print(gaus2)
gaus3 = ThinLense(f=20e-3)*gaus2
print(gaus3)


gaus = GaussianBeam(1064, w=7e-6*1.1)
gaus2 = T(20e-3, 1.0)*gaus
# print(gaus2)
gaus3 = ThinLense(f=20e-3)*gaus2
print(gaus3)
print(gaus3.W(220e-3))
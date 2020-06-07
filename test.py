
from abcd import *
from matrices import *
from gaussian import GaussianBeam
from ray import Ray

gaus = GaussianBeam(1064, w=15.4e-6)

System = ThinLense(f=20e-3)*T(20e-3, 1.0)

gaus2 = T(20e-3, 1.0)*gaus
print(gaus2)

gaus3 = ThinLense(f=20e-3)*gaus2
print(gaus3)
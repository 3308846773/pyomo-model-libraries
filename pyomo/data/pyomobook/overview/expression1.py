from pyomo.core import *

model = AbstractModel()

model.x = Var(initialize=1.0)

def _e(m,i):
  return m.x*i
model.e = Expression([1,2,3],initialize=_e)

instance = model.create()

print value(instance.e[1]) # -> 1.0
print instance.e[1]()      # -> 1.0
print instance.e[1].value  # -> a pyomo expression object

# Change the underlying expression
instance.e[1].value = instance.x**2
# This requires re-preprocessing
instance.preprocess()

#... solve
#... load results

# print the value of the expression given the loaded optimal solution
print value(instance.e[1]) 

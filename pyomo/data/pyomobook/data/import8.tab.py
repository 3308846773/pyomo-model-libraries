from pyomo.core import *

model = AbstractModel()

model.I = Set(initialize=['I1', 'I2', 'I3', 'I4'])
model.A = Set(initialize=['A1', 'A2', 'A3'])
model.U = Param(model.A,model.I)

instance = model.create('import8.tab.dat')

print('A '+str(sorted(list(instance.A.data()))))
print('I '+str(sorted(list(instance.I.data()))))
print('U')
for key in sorted(instance.U.keys()):
    print(cname(instance.U,key)+" "+str(value(instance.U[key])))

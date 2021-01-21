import os
p=os.getcwd()
f=os.listdir(p)
os.remove(f[1::])
print(f)
import matplotlib.pyplot as plt

def func(x, y):
    lines = len(file1)
    for i in range(1,lines):
        si = file1[i].split()
        x.append(float(si[0]))
        y.append(float(si[1]))
    return x, y

file = open("PZ_Mon_v_radial_1.dat", "r")
file1 = file.readlines()
x = []
y = []
f = func(x, y)
print(x)
print(y)
plt.scatter(x, y, color="red", marker='.')
plt.xticks(fontsize=5)
plt.xlabel('MJD')
plt.ylabel('Vr')
plt.show()
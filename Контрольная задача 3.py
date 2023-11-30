import astropy.io.fits as asp
import matplotlib.pyplot as plt

x0 = 670
y0 = 1655
r = int(input('Введите диапазон: '))

#x1 = 633
#x2 = 706
#y1 = 1614
#y2 = 1694

X = []
Y = []
VX = []
VY = []
ffile = asp.open("/Users/admin/Desktop/Pyton/prog/v523cas60s-001(1).fit")
ffile.info()
scid = ffile[0].data
ffile.close()

for i in range(y0-r, y0+r):
    Y.append(i)
    VY.append(scid[i][x0])
for j in range(x0-r, x0+r):
    X.append(j)
    VX.append(scid[y0][j])
print('X=', X)
print('Y=', Y)
print('-------')
print('VY=', VY)
print('VX=', VX)

plt.figure()

plt.subplot(3, 2, 1)
plt.plot(X, VX, color='red')
plt.xlabel('Координаты X')
plt.ylabel('Величина')

plt.subplot(3, 2, 3)
plt.plot(Y, VY)
plt.xlabel('Координаты Y')
plt.ylabel('Величина')

plt.show()
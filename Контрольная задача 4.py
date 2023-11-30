import astropy.io.fits as asp

ffile = asp.open("/Users/admin/Desktop/Pyton/prog/v523cas60s-001(1).fit")
ffile.info()
scid = ffile[0].data
ffile.close()


x0 = 670
y0 = 1655
r = 11
rf = 28
v = 0 # счетчик количества пикселей кольца
d = 0 # счетчик количества пикселей звезды
E = 0
Eo = 0
t = ffile[0].header['exptime']
#(x - x0)**2 + (y - y0)**2 = r**2

for i in range(y0-rf, y0+rf): # координаты y
    for j in range(x0-rf, x0+rf): # координаты x
        g = (j - x0)**2 + (i - y0)**2
        if g <= r**2:
            d = d + 1
            E = E + scid[i][j]
        if g >= r**2:
            if g <= rf**2:
                v = v + 1
                Eo = Eo + scid[i][j]

m = E/t
Ecr = Eo/(t*v)
Nf = Ecr*d
I = m - Nf

print('-'*20)
print('            Eo', '     E', '    t')
print(v, d,  Eo, E, t)
print(rf, r)
print(f'm = {m} \nEcr = {Ecr} \nNf = {Nf} \n---------- \nI = {I}')
#for i in range(len(X)):
    #x = X[i]
    #y = Y[i]
    #g = (x - x0)**2 + (y - y0)
    #if g <= r



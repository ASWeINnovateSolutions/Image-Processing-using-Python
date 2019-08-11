#FFT 2D;

import cmath
import math

N = int(input("Enter No. of elements: "))
C=[]
for i in range(0, N):
    C.append([])
    for j in range(0, N):
        C[i].append(int(input()))

G=[]
for i in range(0, N):
    G.append([])

for u in range(0, N):
    for v in range(0, N):
        expn = 0.0
        for x in range(0, N):
            for y in range(0, N):
                expn = expn+((cmath.exp((-1j*2*math.pi*int(u)*int(x))/N)*cmath.exp((-1j*2*math.pi*int(v)*int(y))/N))*C[x][y])
        G[u].append((1.0/cmath.sqrt(N))*(1.0/cmath.sqrt(N))*expn)
print(G)
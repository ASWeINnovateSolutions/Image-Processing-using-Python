#DCT 2D;

import math
from scipy.fftpack import dct

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
        sum = 0.0
        for x in range(0, N):
            for y in range(0, N):
                if u==0:
                    alphaU = float(math.sqrt(1.0/N))
                else:
                    alphaU = float(math.sqrt(2.0/N))
                if v==0:
                    alphaV = float(math.sqrt(1.0/N))
                else:
                    alphaV = float(math.sqrt(2.0/N))
                sum = sum + float((math.cos(((2*x+1)*math.pi*u)/(2*N))*math.cos(((2*y+1)*math.pi*v)/(2*N)))*C[x][y])
        G[u].append(sum*alphaU*alphaV)
print(G)
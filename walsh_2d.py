import math
print("2 Dimensional Walsh Transform.")
N = int(input("Enter N: "))
n = 0
f = []

def FindBinary(num):
    t_num = num
    bin = str("")
    if t_num==0:
        bin =str("0")
    while t_num!=0:
        d = t_num%2
        if d==0:
            bin = bin+ str("0")
        if d==1:
            bin = bin+ str("1")
        t_num = int(t_num/2)
    bin = bin+"0000000"
    return bin

def FindInnerSum(u, x, v, y, N, i):
    if N==4:
       # print("Yeah n is 2!")
        n=2
    if N==2:
       # print("Yeah n is 1")
        n=1
    if N==8:
        n = 3
    b_u= str("")
    b_x= str("")
    b_v= str("")
    b_y= str("")
    b_u = FindBinary(u)
    b_x = FindBinary(x)
    b_v = FindBinary(v)
    b_y = FindBinary(y)
    sum = ((float(b_u[n-1-i])*float(b_x[i])) + (float(b_v[n-1-i])*float(b_y[i])))
    return sum



if N==2:
    n = 1
if N==4:
    n = 2
if N==8:
    n = 3

for i in range(0, N):
    f.append([])
    for j in range(0,N):
        f[i].append(int(input()))

W = []
for i in range(0, N):
    W.append([])

for u in range(0, N):
    for v in range(0,N):
        ans =0.0
        for x in range(0, N):
            for y in range(0,N):
                product = 1.0
                for i in range(0, n):
                    innerSum = float(FindInnerSum(u, x, v, y, N, i))
                    product = product*math.pow(-1, innerSum)
                ans = ans+float((product*f[x][y]))
        W[u].append(ans*math.sqrt(1.0/N)*math.sqrt(1.0/N))
print(W)
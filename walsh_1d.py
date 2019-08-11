import math
print("1 Dimensional Walsh Transform.")
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

def FindInnerSum(u, x, N, i):
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
    b_u = FindBinary(u)
    b_x = FindBinary(x)
    sum = (float(b_u[n-1-i])*float(b_x[i]))
    return sum



if N==2:
    n = 1
if N==4:
    n = 2
if N==8:
    n = 3

for i in range(0, N):
    f.append(int(input()))

W = []
for u in range(0, N):
    ans = 0.0
    for x in range(0, N):
        product = 1
        for i in range(0, n):
            innerSum = FindInnerSum(u, x, N, i)
            product = product*math.pow(-1, innerSum)
        ans = ans+(product*f[x])
    W.append(ans*math.sqrt(1.0/N))

print(W)
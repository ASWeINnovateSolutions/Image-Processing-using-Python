#FFT 1D
import cmath
import math

def main():
    f=[]
    g=[]
    n=int(input("Enter Linit of input Array: "))
    for i in range(0, n):
        f.append(int(input()))
    for u in range(0,n):
        sum=float(0)
        for x in range(0,n):
            expn = cmath.exp((-1j*2*cmath.pi*int(u)*int(x))/n)*f[x]
            sum +=expn;
    
        ans = (1/cmath.sqrt(n))*sum
        g.append(ans)

    print(g)

if __name__=="__main__":
    main()






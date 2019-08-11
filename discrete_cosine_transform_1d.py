# DCT 1 dimensional
import math

def main():
    N = int(input("Enter no. of elements: "));
    c=[];
    g=[];
    for i in range(0, N):
        c.append(int(input()));
    for u in range(0, N):
        sum = 0;
        for x in range(0, N):
            if(u==0):
                alphaU = float(1.0/math.sqrt(N));
            else:
                alphaU = float(math.sqrt(2.0/N));
            sum = sum+ float((math.cos(((2*x+1)*math.pi*u)/(2*N)) * c[x]));
        sum = alphaU*sum;
        g.append(sum);
    print(g);


if __name__ == "__main__":
    main();

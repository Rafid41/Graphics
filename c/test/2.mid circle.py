import matplotlib.pyplot as plt

x=[]
y=[]

r= 5
xc, yc= 0,0

xk,yk= 0, r
pk= (5/4)-r

x.append(xk)
y.append(yk)

while x<=y:
    if pk<0:
        xk=xk+1
        pk=pk + 2 * xk + 1

    else:
        xk=xk+1
        yk=yk-1
        pk=pk+ 2*xk + 1- 2*yk

    x.append(xk)
    y.append(yk)

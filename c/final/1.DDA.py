#DDA RAN
import matplotlib.pyplot as plt

x0,y0=1,1
xe,ye=100,200

xk=x0
yk=y0

def compareX(xk):
    if x0 < xe:
        if xk >= xe:
            return True
        else:
            return False

    else:
        if xk <= xe:
            return True
        else:
            return False


def compareY(yk):
    if y0 < ye:
        if yk >= ye:
            return True
        else:
            return False

    else:
        if yk <= ye:
            return True
        else:
            return False



#main

m=float((ye - y0)/(xe - x0))

x=[]
y=[]
x.append(x0)
y.append(y0)



while True:
    if compareX(xk) and compareY(yk):
        break

    if m>0 and m<= 1:
        xk= xk+1
        yk= yk+m

    elif m>=-1 and m<=0:
        xk = xk - 1
        yk = yk - m

    elif m>1:
        xk= xk + (1/m)
        yk = yk + 1
    else:  # m<-1
        xk = xk - (1 / m)
        yk = yk - 1




    x.append(round(xk))
    y.append(round(yk))

    #x.append(xk)
    #y.append(yk)


plt.plot(x, y, marker='o')
plt.show()
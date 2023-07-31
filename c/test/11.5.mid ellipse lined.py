import matplotlib.pyplot as plt

def midEllipse(rx, ry, xc, yc):

    x=0
    y=ry

    pt=[]

    plt.plot(xc, yc, marker='o')

    #initial parameters of R1
    d1= (ry*ry) - (rx*rx *ry) + (0.25*rx*rx)
    dx= 2* ry * ry *x
    dy= 2* rx * rx *y

    #for R1
    while dx<dy:
        pt.append((x+xc, y+yc))
        pt.append((-x + xc, y + yc))
        pt.append((x + xc, -y + yc))
        pt.append((-x + xc, -y + yc))



        if d1<0:
            x=x+1
            dx= dx+(2*ry*ry)
            d1=d1+dx+ (ry*ry)

        else:
            x=x+1
            y=y-1
            dx = dx + (2 * ry * ry)
            dy= dy-(2*rx*rx)
            d1 = d1 + dx -dy+ (ry*ry)

    #decision parameter of R2
    d2=(((ry*ry) * ((x+0.5) * (x+0.5))) + ((rx*rx) * ((y-1) * (y-1))) - (rx*rx * ry*ry))

    #R2 points
    while y>=0:
        pt.append((x + xc, y + yc))
        pt.append((-x + xc, y + yc))
        pt.append((x + xc, -y + yc))
        pt.append((-x + xc, -y + yc))


        if d2>0:
            y=y-1
            dy= dy-(2*rx*rx)
            d2=d2+(rx*rx)-dy

        else:
            y=y-1
            x=x+1
            dx = dx + (2 * ry * ry)
            dy = dy - (2 * rx * rx)
            d2 = d2 + dx - dy + (rx * rx)

    pt.sort()
    plt.plot(pt)

#main
midEllipse(10, 15, 50, 50)
plt.grid(True)
plt.show()


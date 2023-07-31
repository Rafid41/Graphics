import matplotlib.pyplot as plt

def midCircle(xc,yc,r):
    x=r
    y=0

    #center
    plt.plot(xc, yc, marker='o')

    plt.plot(x+xc, y+yc, marker='o')

    if r>0:
        plt.plot(x + xc, -y + yc, marker='o')
        plt.plot(y + xc, x + yc, marker='o')
        plt.plot(-y + xc, x + yc, marker='o')

    #p=1-r
    p=(5/4)-r

    while x>y:
        y=y+1

        #if inside
        if p<=0:
            p=p+ 2*y +1

        #if outside
        else:
            x=x-1
            p = p + 2*y - 2*x + 1

        #if all points calculated
        if x<y:
            break

        #other octants
        plt.plot(x+xc, y+yc, marker='o')
        plt.plot(-x + xc, y + yc, marker='o')
        plt.plot(x + xc, -y + yc, marker='o')
        plt.plot(-x + xc, -y + yc, marker='o')


        #if points on the line
        if x!=y :
            plt.plot(y + xc, x + yc, marker='o')
            plt.plot(-y + xc, x + yc, marker='o')
            plt.plot(y + xc, -x + yc, marker='o')
            plt.plot(-y + xc, -x + yc, marker='o')


#main

midCircle(0,0,3)
plt.grid(True)
plt.show()
s="2000-2020"

l=s.split("-")
x=0
for i in range(int(l[0]), int(l[1])+1):
    if i%400==0:
        x+=1
    elif i%100==0:
        pass
    elif i%4==0:
        x+=1

print(x)
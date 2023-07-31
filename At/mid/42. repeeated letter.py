s='thequickbrownfoxjumpsoverthelazydog'

d=dict()

for i in s:
    d[i]=0

for i in s:
    d[i]+=1

l=list(d.items())

for z in l:
    if z[1]>1:
        print(z[0]," = ",z[1])



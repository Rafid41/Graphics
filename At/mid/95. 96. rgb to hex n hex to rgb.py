b="(255,247,229)"
b=b.replace('(','')
b=b.replace(')','')

l=b.split(',')

s=""
for i in l:
    b=hex(int(i))
    s+= b.replace(b[0:2],'')

print(s)

for i in range(0,len(s),2):
    print(int(s[i:i+2], base=16), end=",")

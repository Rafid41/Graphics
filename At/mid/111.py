#ascii of char=  ord(char)

l="Python Tutorial"

for i in l:
    if i!=' ':
        if ord(i)<97:
            print(ord(i)-64,end=" ")
        else:
            print(ord(i) - 96, end=" ")
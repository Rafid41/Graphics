def duplicate(s):


    l=s.split()

    for s in l:
        for i in range(len(s)):
            for j in range(len(s)):
                if i!=j and s[i]==s[j]:
                    return "duplicate"

    return "no duplicate"


print(duplicate("eghd7uf rt3"))
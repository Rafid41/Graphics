
def lng(i,s1,s2,s,sz):
    #print(s1)
    if i<0:
        return sz,s

    if s1 in s2 and sz<len(s1):
        s=s1
        sz=len(s1)

        return sz,s
    k=s1.replace(s1[i],"")

    p=lng(i-1,k,s2,s,sz)

    q=lng(i-1,s1,s2,s,sz)

    return max(p,q)




s1 = 'a87bcdwdefgh'
s2 = 'xswerabcdwd'



sz,s=lng(len(s1)-1,s1,s2,'',0)
print(s)


'''
from difflib import SequenceMatcher 
  
def longest_Substring(s1,s2): 
  
     seq_match = SequenceMatcher(None,s1,s2) 
  
     match = seq_match.find_longest_match(0, len(s1), 0, len(s2)) 
  
     # return the longest substring 
     if (match.size!=0): 
          return (s1[match.a: match.a + match.size])  
     else: 
          return ('Longest common sub-string not present')  

s1 = 'abcdefgh'
s2 = 'xswerabcdwd'
print("Original Substrings:\n",s1+"\n",s2)
print("\nCommon longest sub_string:")
print(longest_Substring(s1,s2))

'''
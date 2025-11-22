# input= s1="abcd"
# s2="ram"
# output ="arbacmd"
s1="abcd"
s2="ram"
output=""
i,j=0,0
while i<len(s1) or j<len(s2):
    if i<len(s1):
        output+=s1[i]
        i=i+1
    if j<len(s2):
        output+=s2[j]
        j=j+1
print(output)
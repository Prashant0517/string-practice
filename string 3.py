#input=aaaabbbcc
#output=a4b3c2

string="aaaabbbcc"
prev=string[0]
output=""
c=1
i=1
while i<len(string):
    if string[i]==prev:
        c+=1
    else:
        output+=prev+str(c)
        prev=string[i]
        c=1
    if i==len(string)-1:
        output+=prev+str(c)
    i=i+1
print(output)
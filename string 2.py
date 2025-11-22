#input=aaaabbbccz
#output=4a3b2c1z

string="aaaabbbccz"
c=1
output=""
i=1
prev=string[0]
while i<len(string):
    if string[i]==prev:
        c=c+1
    else:
        output+=str(c)+prev
        c=1
        prev=string[i]
    if i==len(string)-1:
        output+=str(c)+prev
    i+=1
print(output)
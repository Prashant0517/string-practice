#input=a4c3n3
#output=aecfnq

string="a4c3n3"
output=""
for i in string:
    if i.isalpha():
        output+=i
        ch=i
    else:
        d=int(i)
        new=chr(ord(ch)+d)
        output+=new

print(output)

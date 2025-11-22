# reverse string by loop
s="my name is prashant"
i=len(s)-1
output=""
while i>=0:
    output+=s[i]
    i=i-1
print(output)
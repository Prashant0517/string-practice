#reverce every word of the string
s="my name is prashant"
i=len(s)-1
output=""
while i>=0:
    output+=s[i]
    i=i-1

print(output)

# reverse the each word one by one
s="my name is prashant"
l=s.split()
l1=[]
for word in l:
    l1.append(word[ : :-1])
output=" ".join(l1)
print("reverse word one by one:",output)
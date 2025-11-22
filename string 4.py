#input=A4B3C2
#output=ACD123
string="A4D2C1"
alphabet=[]
digit=[]
for i in string:
    if i.isalpha():
        alphabet.append(i)
    else:
        digit.append(i)
output="".join(sorted(alphabet)+sorted(digit))
print(output)
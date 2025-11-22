#seprate even and odd place charecters of string

s="jay shree ram"
i=0
print("even charecter of string:")
while i<len(s):
    print(s[i])
    i=i+2
i=1
print("odd charecter of string:")
while i<len(s):
    print(s[i])
    i=i+2

# by using sliceing
print("by using slicing even:",s[0: :2])
print("by using slicing odd:",s[1: :2])
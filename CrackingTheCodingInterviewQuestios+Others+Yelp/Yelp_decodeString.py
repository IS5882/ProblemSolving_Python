s = "abc3[a]"
x=""
print(s)

for i in range(len(s)):
    if s[i].isalpha():
        x=x+s[i]
    elif s[i].isdigit() and (s[i+1]=="["):
        j=0
        print(j)
        while(j <= int(s[i]) and s[i+j+2] != "]" and (i+j)<len(s)-2):
            if(s[i+j])
            j = j + 1
            x=x+s[i+j+1]






print(x)
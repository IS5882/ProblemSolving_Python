import re

S="The   fox jumped            over         the log."

print(S)
print(" ".join(S.split()))
print(S)

print(re.sub(' +',' ',S))
print(re.sub(' +',' ',S))
print("a".join(S.split()))
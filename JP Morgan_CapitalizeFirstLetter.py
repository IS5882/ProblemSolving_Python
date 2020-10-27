def capitalizeFirstLetter(s):

    res=""

    for word in s.split():
        #newWord=""
        if word[0].islower():
            res+=word[0].upper()+word[1:]+" "
        else:
            res+=word+" "

    return res[:-1]

print(capitalizeFirstLetter("hello this is injy"))
print(capitalizeFirstLetter("one two 3"))
print(capitalizeFirstLetter("  k"))

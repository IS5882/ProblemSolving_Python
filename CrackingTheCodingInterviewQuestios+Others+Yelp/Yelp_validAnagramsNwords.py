#def validAnagrams(words):
 #   return (sorted(words[i]for i in range(len(words)))

#print(validAnagrams(['cat','tac']))
name = input("Enter the words you want to check seperated by space? ")
x=name.split()
print(x)
j=0
for i in range(len(x)):
    print(x[i])
    j=i+1
    while j in range(len(x)):
        print(x[j])
        if(sorted(x[i])==sorted(x[j])):
            print(" ANAGRAMSS")
            j = j + 1
            continue

        else:
            print("not Anagrams")
            break #break from while

    break#break from for



beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

if (endWord not in wordList):
    print ("not in wordList")

word_dict = set(wordList)
print(wordList)
print(word_dict)
startQ=set()
startQ.add(beginWord)

print(len(startQ))
print(startQ)

for i in startQ:
    print(i)
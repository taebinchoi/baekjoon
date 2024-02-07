word = input().upper()
wordlist = list(set(word))

totword = []
for i in wordlist:
    count = word.count
    totword.append(count(i))

if totword.count(max(totword)) > 1:
    print("?")
else:
    print(wordlist[(totword.index(max(totword)))])
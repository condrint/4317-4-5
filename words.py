words = set()
with open('words.txt', 'r') as f:
    for line in f:
        words.add(line.strip())


print('pairs with -e added to end')
for word in words:
    if len(word) < 4:
        continue
    if word + 'e' in words:
        print(word, word + 'e')
        print('')

print('pairs differing by one character')
for word in words:
    if len(word) < 4:
        continue
    for i in range(len(word)):
        newWord = word[0:i] + word[i + 1:]
        if newWord in words:
            print(word, newWord)
            print('')


str = "This is an awesome occasion. This has never happened before."

# key:value

char_occurances = {} #[]

for char in str:
    char_occurances[char] = char_occurances.get(char, 0) + 1

print(char_occurances)

word_occurances = {} #[]

for word in str.split():
    word_occurances[word] = word_occurances.get(word, 0) + 1

print(word_occurances)
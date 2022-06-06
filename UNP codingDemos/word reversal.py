word = 'bismillah'
rev = ''
# itearate over a sequence , counting backwards
for x in range(len(word) -1, -1, -1):
    # Concatanate character at index x
    rev += word[x]
print(rev)
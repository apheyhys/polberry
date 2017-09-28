vowels = set('aeiou')
word = input()
i = vowels.intersection(set(word))
for p in i:
    print(p)
        
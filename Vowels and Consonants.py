def num_vowels(string):
    no_spaces = string.strip()
    lower = no_spaces.lower()
    vowels = 0
    sometimes_vowels = 0
    for i in lower:
        if i.isalpha():
            if i == 'a' or i == 'e' or i == 'i' or i =='o' or i == 'u':
                vowels += 1
            elif i == 'y':
                sometimes_vowels += 1
    print(f'Vowels: {vowels}\nSometimes vowels (y): {sometimes_vowels}')


def num_consonants(string):
    no_spaces = string.strip()
    lower = no_spaces.lower()
    consonants = 0
    for i in lower:
        if i.isalpha():
            if i != 'a' and i != 'e' and i != 'i' and i != 'o' and i != 'u' and i != 'y':
                consonants += 1
    print(f'Consonants: {consonants}')

sentence = input('Enter a sentence:\n')
num_vowels(sentence)
num_consonants(sentence)
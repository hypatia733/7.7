# I was going to give you my comments by submitting issues, but that's a lengthy process and I want to be done with this tonight lol.
# The next issue is that when you use split(), it creates an array. Each item in that array is a word, since split() defaults to spaces
# A string is immutable, so you can't use .replace to change single characters, or add the 'ay' to the end of the word.
# Therefore, I'm going to change it so that we split each word into its own array as well, except this array will contain each character
# Then, we will manipulate each word inside that array, reassemble it, and print it.
# We do this for each word, resulting in the full sentence.

def pig_latin(input):
    word_array = input.split()
    char_array = []
    for word in word_array:
        char_array.clear() # Gotta empty the array every time since we only want the letters from the current word
        for letter in word:
            char_array.append(letter) # You can also use the list[str] method to create an array (or "list") of the letters
        first_letter = char_array[0]
        char_array.remove(first_letter)
        char_array.append(first_letter)
        char_array.append('ay')
        new_word = ''.join(char_array[0:len(char_array)]) # re-assemble the items in the list to a string
        print(new_word, end=' ')
    return

sentence = input('Enter a sentence\n')
pig_latin(sentence)

# Final note - I would have liked to have the program take note of whether the first letter is capital, change it to lower when it gets moved,
# and then change to new first letter to upper (only if the original first was upper), but I don't have time tonight.

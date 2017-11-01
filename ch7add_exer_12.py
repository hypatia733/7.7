def pig_latin(sentence):
    sentence = sentence.split()
    for word in sentence:
        word = word.replace(',', word[0])+'ay '
        word = word.replace(word[0], '')
        print(word, end = '')
    return 

sentence = input('Enter a sentence\n')
pig_latin(sentence)


def pig_latin(sentence):
    sentence = sentence.split(',')
    i = 0
    for word in sentence:
        word = word.replace(word[-1], word[0])+'ay '
        word = word.replace(word[0], '')
        print(word, end = '')
    return 

sentence = input('Enter a sentence\n')
pig_latin(sentence)

import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read().translate({ord(i): None for i in '\n'}).split(' ')
    # print(words)
    punc = ['.', '!', '?']
    starters = [word for word in words if word[0].isupper()]
    enders = [word for word in words if word[-1] in punc]
    table = {}
    print(enders)

# TODO: analyze which words can follow other words
# Your code here
    for i in range(len(words) - 1):
        if words[i] not in table:
            table[words[i]] = [words[i+1]]
        else:
            table[words[i]].append(words[i+1])

    print(table)
# TODO: construct 5 random sentences
# Your code here
    def get_new_word(word):
        new_word = random.choice(table.get(word))
        return new_word

    def sentence_constructor(word):
        sentence = str(word)
        while word not in enders:
            word = get_new_word(word)
            sentence += word + ' '
    
        print(sentence)
        return sentence

sentence_constructor(random.choice(starters))
sentence_constructor(random.choice(starters))
sentence_constructor(random.choice(starters))
sentence_constructor(random.choice(starters))
sentence_constructor(random.choice(starters))
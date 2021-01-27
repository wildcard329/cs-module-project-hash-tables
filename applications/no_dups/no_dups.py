def no_dups(s):
    # Your code here
    if s == '':
        return s
    s = s.split(' ')
    words = set()
    words_list = []
    for word in s:
        if word not in words:
            words.add(word)
            words_list.append(word)

    string = ' '.join(words_list)
    string = string.strip()

    # print(f'"{string}"')
    print(words_list)
    return string


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
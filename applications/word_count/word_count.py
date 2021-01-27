def word_count(s):
    # Your code here
    counter = {}
    words = s.translate({ord(i): None for i in '":;,.-+=/\|][}{)(*^&'}).lower().split()
    for word in words:
        if word not in counter:
            word = word.lower()
            counter[word] = 0
        counter[word] += 1
    return counter


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
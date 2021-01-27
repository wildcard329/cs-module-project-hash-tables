# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
with open("ciphertext.txt") as f:
    text = f.read()
    table = {}
    freq_check = []
    for char in text:
        if not char.isalpha():
            continue
        else:
            if char not in table:
                table[char] = 0
            table[char] += 1

    for key in table:
        freq_check.append((table[key], key))

    freq_check.sort(reverse = True)

    freq_list = []
    for i in range(len(freq_check)):
        freq_list.append(freq_check[i][1])

    alpha = 'a'
    alpha_list = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U', 'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']
    decoder = {}

    for i in range(len(alpha_list)):
        decoder[freq_list[i]] = alpha_list[i]
    
    def decode(s):
        message = ''
        for char in s:
            if char.isalpha():
                message += decoder[char]
            else:
                message += char
        print(message)
        return message
    # print(len(decoder))
    print(decode(text))
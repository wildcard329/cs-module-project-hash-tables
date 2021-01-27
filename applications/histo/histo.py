# Your code here
with open("robin.txt") as f:
    words = sorted(f.read().translate({ord(i): None for i in '":;,.-+=/\|][}{)(*^&'}).lower().replace('\n', ' ').split(' '))
    counter = {}
    for word in words:
        if word not in counter:
            counter[word] = 0
        counter[word] += 1

    counter_list = []
    for key in counter:
        counter_list.append((counter[key], key))
    counter_list.sort(reverse = True)

    for entry in counter_list:
        print(entry[1],'\b: ','#'*entry[0])
    # print(counter_list)
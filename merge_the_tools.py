def merge_the_tools(string, k):
    # your code goes here
    length = len(string)
    split_length = int(length/k)
    string_list = []
    for i in range(split_length):
        temp = string[i * k : (i + 1) * k]
        string_list.append(temp)
    for i in string_list:
        x = "".join(dict.fromkeys(i))
        print(x)

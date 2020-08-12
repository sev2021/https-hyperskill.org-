# Create your own split() method:

def mysplit(inp_string, separat = " "):
    split_list = []
    word = ""
    for i in inp_string:
        if i != sepeparat:
            word += i
        else:
            split_list.append(word)
            word = ""
    split_list.append(word)
    return split_list

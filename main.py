# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    '''reading file contents'''
    with open(filename) as files:
        lines = files.read().split()
    return lines


def count_words():
    '''counting word occurences'''
    text = read_file_content("./story.txt")
    words = {}
    for word in text:
        if word not in words:
            words[word] = 1
        else:
            words[word] += 1
    return words

print(count_words())
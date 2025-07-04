# read a text file and return the content 
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()   

# recive a string and return the number of words
def get_num_words(content):
    words = content.split()
    return len(words)

# count number of times a characters apear in text
def get_characters(a):
    text = a.lower()
    counter = {}
    for char in text:
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1
    return counter

# sort characters in alphabetical 
def sort_characters(chars):
    sort_char = dict(sorted(chars.items()))
    return sort_char

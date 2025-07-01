def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()   

def get_num_words(content):
    words = content.split()
    return len(words)




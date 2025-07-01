from stats import get_book_text
from stats import get_num_words

def main():
    path = "books/frankenstein.txt" 
    text = get_book_text(path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    
main()




from stats import get_book_text
from stats import get_num_words
from stats import get_characters

def main():
    path = "books/frankenstein.txt" 
    text = get_book_text(path)
    num_words = get_num_words(text)
    num_chars = get_characters(text)
    print(f"{num_words} words found in the document")
    print(num_chars)
main()




from stats import get_book_text
from stats import get_num_words
from stats import get_characters
from stats import sort_characters

def main():
    path = "books/frankenstein.txt" 
    text = get_book_text(path)
    num_words = get_num_words(text)
    num_chars = get_characters(text)
    sort_chars = sort_characters(num_chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for key, valor in sort_chars.items():
        if str(key).isalpha():
            print(f"{key}: {valor}")

    print("============= END ===============")

main()




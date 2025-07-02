import sys 
from stats import get_book_text
from stats import get_num_words
from stats import get_characters
from stats import sort_characters


def main(argv):
    # get second arg as a path to a book
    text = get_book_text(argv)
    num_words = get_num_words(text)
    num_chars = get_characters(text)
    sort_chars = sort_characters(num_chars)

    # print ordered report 
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {argv}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    # iterate in each value of a dict a print it
    for key, value in sort_chars.items():
        if str(key).isalpha():
            print(f"{key}: {value}")

    print("============= END ===============")

# check that 2 arguments are given
if len(sys.argv) == 2:
    main(sys.argv[1])
else: #if not do an explanation of how to use 
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

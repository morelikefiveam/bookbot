import sys
from stats import get_word_count
from stats import character_count
from stats import sort_on
from stats import report
# Goes through the filepath, opens the specified file and returns it as text 
def get_book_text(filepath):
    with open (filepath) as frankenstein:
        frankenstein_contents = frankenstein.read()

    return frankenstein_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    
    # Makes the text gleaned from above a variable
    book_contents = get_book_text(sys.argv[1])
    # Uses the get_word_count function in stats.py to make the wc a variable
    word_count = get_word_count(book_contents)
    print(f"""""============ BOOKBOT ============
    Analyzing book found at books/frankenstein.txt...
    ----------- Word Count ----------
    Found {word_count} total words""")
    print("--------- Character Count -------")
    character_numbers_dict = character_count(book_contents)
    sorted_list = report(character_numbers_dict) 
    
    for item_dict in sorted_list:
        if item_dict["char"].isalpha():
            print(f"{item_dict['char']}: {item_dict['num']}")
    print("============= END ===============")
    
    

main()
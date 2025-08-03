# Gets the word count by getting the length of the split text
def get_word_count(book_contents):
    word_count = len(book_contents.split())
    
    return word_count

def character_count(book_contents):
    #Makes the contents of the text lowercase
    lower_book_contents = book_contents.lower()
    character_numbers = {

    }
   # If a character occurs in the book for the first time , add it to empty dictionary
   # Otherwise, increase its count in the dictionary 
    for char in lower_book_contents:
        if char in character_numbers:
            character_numbers[char] += 1
        else:
            character_numbers[char] = 1

    return character_numbers
# Tells Python that when the dictionaries are sorted, use the value associated with "num" to sort 
def sort_on(character_numbers):
    return character_numbers["num"]
# Iterates through the dictionary, sorting them into a list
def report(character_numbers):
    sorted_numbers = []
    for char, count in character_numbers.items():
        char_count_dict = {
         "char" : char, "num" : count
        }
        sorted_numbers.append(char_count_dict)
    sorted_numbers.sort(reverse=True, key=sort_on)

    return sorted_numbers



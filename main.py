def main():
    book_path = "books/frankenstein.txt"
    file_contents = get_book_text(book_path)
    word_count = get_book_word_count(file_contents)
    # print(file_contents)
    # print(word_count)
    print(f"--- Begin report of books/{book_path} ---")
    print(f"{get_book_word_count(file_contents)} words found in the document")
    sorted_words_list = get_letter_count(file_contents)
    for letter_dict in sorted_words_list:
        print(f"The `{letter_dict["letter"]} character was found {letter_dict["num"]} times")
    print(f"--- End report ---")

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()
    
def get_book_word_count(file_contents):
    words = file_contents.split()
    return len(words)

def get_letter_count(file_contents):
    words_list = []
    letter_counts = {}
    lowercase_strings = file_contents.lower()
    for letter in lowercase_strings:
        if(letter.isalpha() == False):
            continue

        if(letter.isalpha() and letter not in letter_counts):
            letter_counts[letter] = 1
        else:
            letter_counts[letter] += 1

    for letter in letter_counts:
        words_list.append({"letter": letter, "num": letter_counts[letter] })

    words_list.sort(reverse=True, key=sort_on)
    
    return words_list
    

def sort_on(dict):
    return dict["num"]

main()

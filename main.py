def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    # print(text)
    # print(count_words(text))
    # print(count_chars_num(text))
    print(f"--- Begin report of {book_path} ---")
    word_num = count_words(text)
    print(f"{word_num} words found in the document")
    print()

    chars_dict = count_chars_num(text)
    sorted_chars_list = sort_chars_num(chars_dict)
    for char_item in sorted_chars_list:
        char = char_item["char"]
        num = char_item["num"]
        if char.isalpha():
            print(f"The '{char}' character was found {num} times") 


    print("--- End report ---")

def count_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_chars_num(text):
    chars_num = {}
    for char in text.lower():
        if char in chars_num:
            chars_num[char] += 1
        else:
            chars_num[char] = 1
    return chars_num

def sort_char(char_dict):
    return char_dict["num"]

def sort_chars_num(chars_dict):
    chars_array = []
    for key in chars_dict:
        char_item = {"char": key, "num": chars_dict[key]}
        chars_array.append(char_item)
    chars_array.sort(reverse=True, key=sort_char)
    return chars_array
    
main()
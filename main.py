from stats import word_count
from stats import charater_count
from stats import processed_dict_report
import sys

def get_book_text(path_to_file):
    file_contents = ""
    try:
        with open(path_to_file) as f:
            file_contents = f.read()
            return file_contents
    except FileNotFoundError:
        print(f"Error: The file'{path_to_file}' was not found")

#def word_count(content_of_book):
 #   wc = 0
  #  for word in content_of_book.split():
   #     wc += 1
    #return wc


def main():
    args = len(sys.argv)
    if args != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_file = sys.argv[1]
    contents_of_book = get_book_text(path_to_file)
    total_words = word_count(contents_of_book)
    total_chars = charater_count(contents_of_book)
    sorted_contents = processed_dict_report(total_chars)
    if args ==2 :
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path_to_file}")
        print("---------------- word count ---------------")
        print(f"Found {total_words} total words")
        print("------------- Character count ---------------")
        for item in sorted_contents:
            if item["char"].isalpha():
                print(f"{item['char']}: {item['num']}")
        print("============== End ================")
    else:
        print("unable to retrive book text.")
if __name__ == "__main__":
    main()

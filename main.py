import string

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    # word_count = count_words(text)
    # print(word_count)
    # print(analyze_letters(text))
    report(text)

def count_words(text):
    count = len(text.split())
    return count

def analyze_letters(text):
    lowercase = text.lower()
    analysis = dict.fromkeys(string.ascii_lowercase, 0)
    for letter in lowercase:
        if letter.isalpha():
            analysis[letter] += 1
    sorted_analysis = sorted(analysis.items(), key=lambda x: x[1], reverse=True)
    return sorted_analysis


def report(text):
    letter_counts = analyze_letters(text)
    print(f"\n-------------------BEGINNING ANALYSIS-------------------\n\n{count_words(text)} words were found in the document.\n")
    for i in range(len(letter_counts)):
        print(f"The letter {letter_counts[i][0]} occured {letter_counts[i][1]} time(s)")

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
def countChars(words):
    chars = {}

    for word in words:
        word = word.lower()

        for w in word:
            if w in chars:
                chars[w] += 1

            else:
                chars[w] = 1

    return chars

def report(words, chars):
    print("--- Begin report of books/frankenstein.txt ---")

    print(f"{len(words)} words found in the document")
    print()

    chars = dict(sorted(chars.items(),key=lambda item: item[1], reverse=True))
    
    for c in chars:
        if c.isalpha():
            print(f"The {c} character was found {chars[c]} times")

    print()
    print("--- End report ---")

def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()

    words = file_contents.split()
    chars = countChars(words)

    report(words, chars)
    

main()
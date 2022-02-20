import random
def main():
    # read arabic words
    with open("arabic-wordlist-1.6.txt", encoding="utf-8") as words_f:
        words = words_f.readlines()
        # remove harakat and newline from words
        extras = ["\u064B", "\u064C", "\u064D", "\u064E", "\u064F", "\u0650", "\u0652", "\n"]
        words = [replace_group(word, extras) for word in words]
        
        #Keep 5 letter words only
        words = filter(is_5_letters, words)
        words = list(words)

        
        #Keep 5 letter words only
        words = filter(is_5_letters, words)
        words = list(words)

        # removes words that contain spaces (_) or colons (:)
        words = filter(lambda word: not (("_" in word) or (":" in word)), words)
        words = list(words)

        # Replace all variants of alif (أ، إ، آ) with bare alif (ا).
        alifs = ["\u0622", "\u0623", "\u0625"]
        words = [replace_group(word, alifs, replace_by="\u0627") for word in words]

        #remove duplicates 
        words = list(set(words))

        # randomize word order
        random.seed(123)
        words = sorted(words, key = lambda word: random.random())


    # write output to file
    with open("5-letter-ar-words.txt", "w+", encoding="utf-8") as new_words_f:
        new_words_f.write("\n".join(words))

def is_5_letters(word: str) -> bool:
    '''
    Checks if a word is 5 letters.
    '''
    return len(word) == 5

def replace_group(word: str, group: list, replace_by: str = "") -> str:
    """
    Replace multiple strings in a word.
    """

    for el in group:
        word = word.replace(el, replace_by)
    
    return word

if __name__ == "__main__":
    main()
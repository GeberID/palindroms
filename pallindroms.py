
import sys
import cProfile
from pprint import pprint


def load(file :'file') -> 'None':
    """Open file and save file_words"""
    try:
        with open(file) as words_dict:
            word_list = words_dict.read().strip().split('\n')
            word_list = [i.lower() for i in word_list]
        return word_list
    except Exception as err:
        print("Error: ",err ,file = sys.stderr)
        sys.exit(1)
    print(word_list)


def search_pallindroms(list:'file_words') -> list:
    """Search palindroms"""
    pall_list = [i for i in list if i[::-1]==i and len(i)>1]
    pprint (pall_list)


def search_palingrams(list:'file_words') -> list:
    """Отыскать палинграммы в словаре."""
    pali_list = []
    words = set(list)
    for word in words:
        end = len(word)
        rev_word = word[::-1]
        if end > 1:
            for i in range(end):
                if word[i:] == rev_word[:end-i] and rev_word[end-i:] in words:
                    pali_list.append((word,rev_word[end-i:]))
                if word[:i] == rev_word[end-i:] and rev_word[:end-i] in words:
                    pali_list.append((rev_word[:end - i],word))
    return pali_list


def check_word_list (list:'file_words') -> list:
    optim_list = [word for word in list if len(word) >1]
    return  optim_list



word_list = load('words_2.txt')
word_list = check_word_list(word_list)
search = search_palingrams(word_list)
pprint(search)
import os


big_dico = {}
words_dico = {}


def dico(file, dico):
    """
    Make temporary dictionary of word in a file
    parameter:
    ------------
    file: file we want to put his word in a dictionary (file)
    dico: the dico we want to place word (dictionary)
    return:
    ------------
    dico : dictionary of word in the file and number of time it appeared (dictionary)
    """
    fh = open(file, 'r')
    lines = fh.readlines()
    symbols = (
        '(', ')', '1', '2', '', '3', '4', '5', '6', '7', '8', '9', '0', '-', 'º', '`', 'þ', '«', '»', 'ª', '$', '²', ':',
        ',',
        ';', '?', '!', '\'', '^', '+', '-', '#', '=', '/', '*', '\\', '\"', '<', '>', '@', '.', '&', '[', ']', '{', '}',
        '%', 'µ', '§', '_', '|', '~')
    for line in lines:
        for word in line.split():
            for symbol in symbols:
                word = word.replace(symbol, '')
            word = word.lower()
            if not word in dico:
                dico[word] = 1
    fh.close()
    return dico


def dico_with_theme():
    """
    Make a dicionary for
    return:
    """
    big_dico = {}
    for archive in os.listdir(f'./archive'):
        for theme in os.listdir(f'./archive/{archive}/sorted'):
            big_dico[theme] = {}
            for file in os.listdir(f'./archive/{archive}/sorted/{theme}'):
                big_dico[theme][file] = {}
                dico(f'./archive/{archive}/sorted/{theme}/{file}', big_dico[theme][file])
    return big_dico


def smart_sort_files(path):
    """
    Sorts the unsorted files in the directory path in the correct repository of the 'sorted' repository.

    Parameters
    ----------
    path: the path of the directory with the unsorted files (int)
    """
    try:
        os.makedirs('./archive')
    except FileExistsError:
        pass
    os.rename('./archive_1', './archive/archive_1')
    os.rename('./archive_2', './archive/archive_2')
    os.rename('./archive_3', './archive/archive_3')
    os.rename('./archive_4', './archive/archive_4')


def pr(word, theme):
    """get the frequency of a word appeared in a file in a theme
    parameter:
    ------------
    word:  (int)
    theme:  (int)

    return:
    ------------
    frequency: number between 0 and 1
    """
    number = len(big_dico[theme])
    frequency = word / number
    return frequency


def get_chances(file, words_dico):
    """
    Returns the chances to sort the file in the directory, checking  the words_dico of the directory.

    Parameters
    ----------
    file: the path of the file to sort (str)
    words_dico: the dico, with as keys the words of the files in the directory, and as values the proportion of files with that
    word (dico)

    Returns
    -------
    chance: the chance the class the file in the directory with words_dico (int)"""
    list_words = []
    fh = open(file, 'r')
    lines = fh.readlines()
    symbols = (
        '(', ')', '1', '2', '', '3', '4', '5', '6', '7', '8', '9', '0', '-', 'º', '`', 'þ', '«', '»', 'ª', '$', '²',
        ':',
        ',',
        ';', '?', '!', '\'', '^', '+', '-', '#', '=', '/', '*', '\\', '\"', '<', '>', '@', '.', '&', '[', ']', '{', '}',
        '%', 'µ', '§', '_', '|', '~')
    for line in lines:
        for word in line.split():
            for symbol in symbols:
                word = word.replace(symbol, '')
            word = word.lower()
            if not word in list_words:
                list_words.append(word)
    chance = 1
    for word in list_words:
        if word in words_dico:
            chance += math.log(words_dico[word])
    for word in words_dico:
        if not word in list_words:
            chance += math.log(words_dico[word])
    fh.close()
    return chance


def get_words_dico(path):
    """
    Returns a dico with, as keys, the words in the files of the directory path, and as values the proportion, in percent,
     of files with that word
    (example: 3 files on 5 has the word 'apple', so the value of the key 'apple' is 60).

    Parameters
    ----------
    path: the path of the directory for which we want the dico (int)

    Returns
    -------
    words_dico: the wanted dico, with as keys the words of the files in the directory path, and as values the proportion, in percent,
    of the files with that word (dico)
    """
    words_dico = {}
    deleted_char = '|@#{[^}]`´~*!§~`_ñú1234567890\\^°$£¤µ%?€&"«ª\'(ñ§úþ)-µ$»ù=:;,<°£¨%+/.?>'
    for file in os.listdir(path):
        fh = open(path+'/'+file, 'r')
        list_words = []
        for line in fh.readlines():
            better_line = ''
            for char in line:
                if char in deleted_char:
                    better_line += ' '
                else:
                    better_line += char
            words = better_line.lower().split()
            for word in words:
                if not word in list_words:
                    list_words.append(word)
        for word in list_words:
            try:
                words_dico[word] += 1
            except:
                words_dico[word] = 1
        fh.close()
    for word in words_dico:
        words_dico[word] = (words_dico[word]/len(1-os.listdir(path)))
    return words_dico


for archive in os.listdir(f'./archive'):
    for theme in os.listdir(f'./archive/{archive}/sorted'):
        print(theme)
        pprint(get_chances(f'./archive/archive_1/unsorted/38888', get_words_dico(f'./archive/{archive}/sorted/{theme}')))


def check_accuracy(path):
    """Check the accuracy of sorted file form a path
    parameter:
    -------------
    path: Where the have been sorted to be checked
    """
    ...

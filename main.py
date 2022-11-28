import os


big_dico = {}

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
    symbols = ('(',')','1','2','3','4','5','6','7','8','9','0','-','º','`','þ','«','»','ª','$','²',':',',',';','?','!','\'','^','+','-','#','=','/','*','\\','\"','<','>','@','.','&','[',']','{','}','%','µ','§','_','|','~')
    for line in lines:
        for word in line.split():
            for symbol in symbols:
                word = word.replace(symbol,'')
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
    frequency = word/number
    return frequency

def get_freq(dict):
    for archive in os.listdir(f'./archive'):
        for theme in os.listdir(f'./archive/{archive}/sorted'):
            for file in os.listdir(f'./archive/{archive}/sorted/{theme}'):


def check_accuracy(path):
    """Check the accuracy of sorted file form a path
    parameter:
    -------------
    path: Where the have been sorted to be checked
    """
    ...
pprint(dico_with_theme())
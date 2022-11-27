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
    symbols = ('(',')','-','º','`','þ','«','»','ª','$','²',':',',',';','?','!','\'','^','+','-','#','=','/','*','\\','\"','<','>','@','.','&','[',']','{','}','%','µ','§','_','|','~')
    for line in lines:
        for word in line.split():
            for symbol in symbols:
                word = word.replace(symbol,'')
            word = word.lower()
            if word in dico:
                dico[word] += 1
            else:
                dico[word] = 1
    fh.close()
    return dico


def dico_per_theme():
    big_dico = {}
    for archive in os.listdir(f'./archive'):
        for theme in os.listdir(f'./archive/{archive}/sorted'):
            big_dico[theme] = {}
            for file in os.listdir(f'./archive/{archive}/sorted/{theme}'):
                dico(f'./archive/{archive}/sorted/{theme}/{file}', big_dico[theme])
    return big_dico

def smart_sort_files(path):
    """Sort unsorted files from a path
    parameter:
    -------------
    path: where the files will be sorted (path)
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
    for x in big_dico[theme]:



def check_accuracy(path):
    """Check the accuracy of sorted file form a path
    parameter:
    -------------
    path: Where the have been sorted to be checked
    """
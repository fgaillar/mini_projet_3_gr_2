import os


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
    symbol = "()-:,;?!'^+-#=/*\"<>@.&[]{}%µ§_|~"
    for line in lines:
        for word in line.split():
            word = ''.join(x for x in word if x not in symbol or x != '')
            if word in dico:
                dico[word] += 1
            else:
                dico[word] = 1
    fh.close()
    return dico


def analyse():
    ...


def dico_per_theme():
    for archive in os.listdir(f'./archive'):
        for theme in os.listdir(f'./{archive}/sorted'):
            for file in os.listdir(f'./{archive}/sorted/{theme}'):
                dico(f'./{archive}/sorted/{theme}/{file}', )


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


def check_accuracy(path):
    """Check the accuracy of sorted file form a path
    parameter:
    -------------
    path: Where the have been sorted to be checked
    """
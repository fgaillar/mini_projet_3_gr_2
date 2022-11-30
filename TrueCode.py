import os
from pprint import pprint
from math import log10


def dico(file, dico, nb_files):
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
    temp_words = []
    fh = open(file, 'r')
    lines = fh.readlines()
    symbols = (
    '(', ')', '-', 'º', '`', 'þ', '«', '»', 'ª', '$', '²', ':', ',', ';', '?', '!', '\'', '^', '+', '-', '#', '=', '/',
    '*', '\\', '\"', '<', '>', '@', '.', '&', '[', ']', '{', '}', '%', 'µ', '§', '_', '|', '~')
    for line in lines:
        for word in line.split():
            for symbol in symbols:
                word = word.replace(symbol, '')
            word = word.lower()
            if word not in temp_words:
                temp_words.append(word)
    for word in temp_words:
        if word in dico:
            dico[word] += 1 / (nb_files + 1)
    fh.close()
    return dico


def give_words(path):
    big_list = []
    for file in os.listdir(path + '/unsorted/'):
        fh = open(path + f'/unsorted/{file}', 'r')
        lines = fh.readlines()
        symbols = (
        '(', ')', '-', 'º', '`', 'þ', '«', '»', 'ª', '$', '²', ':', ',', ';', '?', '!', '\'', '^', '+', '-', '#', '=',
        '/', '*', '\\', '\"', '<', '>', '@', '.', '&', '[', ']', '{', '}', '%', 'µ', '§', '_', '|', '~')
        for line in lines:
            for word in line.split():
                for symbol in symbols:
                    word = word.replace(symbol, '')
                word = word.lower()
                if word not in big_list:
                    big_list.append(word)
        fh.close()
    return big_list


def dico_per_theme(path):
    big_dico = {}
    big_list = give_words(path)
    for theme in os.listdir(path + '/sorted'):
        big_dico[theme] = {}
        nb_files = len(os.listdir(path + f'/sorted/{theme}'))
        for word in big_list:
            big_dico[theme][word] = 1 / (nb_files + 1)
        for file in os.listdir(path + f'/sorted/{theme}'):
            big_dico[theme] = dico(path + f'/sorted/{theme}/{file}', big_dico[theme], nb_files)
    return big_dico


def get_max_dict(dict):
    max = None
    for key in dict:
        if max == None or dict[key] > max:
            max = dict[key]
            max_key = key
    return max_key


def smart_sort_files(path):
    """Sort unsorted files from a path
    parameter:
    -------------
    path: where the files will be sorted (path)
    """

    big_dico = dico_per_theme(path)
    for file in os.listdir(path + '/unsorted/'):
        words = []
        fh = open(path + f'/unsorted/{file}', 'r')
        lines = fh.readlines()
        symbols = (
        '(', ')', '-', 'º', '`', 'þ', '«', '»', 'ª', '$', '²', ':', ',', ';', '?', '!', '\'', '^', '+', '-', '#', '=',
        '/', '*', '\\', '\"', '<', '>', '@', '.', '&', '[', ']', '{', '}', '%', 'µ', '§', '_', '|', '~')
        for line in lines:
            for word in line.split():
                for symbol in symbols:
                    word = word.replace(symbol, '')
                word = word.lower()
                if word not in words:
                    words.append(word)
        percentage = {}
        for theme in big_dico:
            percentage[theme] = 0
            for word in big_dico[theme]:
                if word in words:
                    percentage[theme] += log10(big_dico[theme][word])
                else:
                    percentage[theme] += log10(1 - big_dico[theme][word])
        theme = get_max_dict(percentage)
        fh2 = open(path + f'/sorted/{theme}/{file}', 'w')
        fh2.write(fh.read())
        fh.close()
        fh2.close()


def check_accuracy(path):
    """Check the accuracy of sorted file form a path
    parameter:
    -------------
    path: Where the have been sorted to be checked
    """
    print('checking accuracy of smart sorted texts ...')
    labels_file = open(path + '/labels.txt', 'r')
    lines = labels_file.readlines()
    nb_lines = len(lines)
    nb_accurates = 0
    list_of_files_by_theme = {}
    for line in lines:
        file_name, theme = line.split()
        if theme not in list_of_files_by_theme:
            list_of_files_by_theme[theme] = os.listdir(path + f'/sorted/{theme}')
        if file_name in list_of_files_by_theme[theme]:
            nb_accurates += 1
    labels_file.close()

    print(f'accuracy is {round(nb_accurates / nb_lines * 100, 3)} %')


path = './archive/archive_1'
smart_sort_files(path)
check_accuracy(path)
path = './archive/archive_2'
smart_sort_files(path)
check_accuracy(path)
path = './archive/archive_3'
smart_sort_files(path)
check_accuracy(path)
path = './archive/archive_4'
smart_sort_files(path)
check_accuracy(path)

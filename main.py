
global dyco_freq


dyco_freq = {}
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


def get_frequency():
    themes = os.listdir('./archive_1/sorted')
    for theme in themes:
        for file in os.listdir(f'./archive_1/sorted/{theme}'):
            dico(f'./archive_1/sorted/{theme}/{file}', dyco_freq)
    themes = os.listdir('./archive_2/sorted')
    for theme in themes:
        for file in os.listdir(f'./archive_2/sorted/{theme}'):
            dico(f'./archive_2/sorted/{theme}/{file}', dyco_freq)
    themes = os.listdir('./archive_3/sorted')
    for theme in themes:
        for file in os.listdir(f'./archive_3/sorted/{theme}'):
            dico(f'./archive_3/sorted/{theme}/{file}', dyco_freq)
    themes = os.listdir('./archive_4/sorted')
    for theme in themes:
        for file in os.listdir(f'./archive_4/sorted/{theme}'):
            dico(f'./archive_4/sorted/{theme}/{file}', dyco_freq)
    return dyco_freq

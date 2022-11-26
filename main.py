

def temporary_dico(file):
    """
    Make temporary dictionary of word in a file
    parameter:
    ------------
    file: file we want to put his word in a dictionary (file)
    return:
    ------------
    temp_dico : dictionary of word in a the file and number of time it appeared (dictionary)
    """
    fh = open(file, 'r')
    temp_dico = {}
    lines = fh.readlines()
    symbol = "()-:,;?!'^+-#=/*\"<>@.&[]{}%µ§°_|~"
    for line in lines:
        for word in line.split():
            word = ''.join(x for x in word if x not in symbol)
            if word in temp_dico:
                temp_dico[word] += 1
            else:
                temp_dico[word] = 1
    print(temp_dico)
    fh.close()
    #return temp_dico



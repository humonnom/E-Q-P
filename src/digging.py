import os
from sys import argv

def get_filelist(path):
    path_dir = path
    filelist = os.listdir(path_dir)
    if '.DS_Store' in filelist:
        filelist.remove('.DS_Store')
    return filelist

def print_sentence(word, senlist):
    print(word, ":")
    if len(senlist) == 0:
        print("empty")
    else:
        for item in senlist:
            print(" ", item)
    save = input('Wanna save these?(y/n):')
    if save == 'y':
        path = 'Diglett/' + word + '.txt'
        f = open(path, 'w')
        for item in senlist:
            f.write(item + '\n')
        f.close()
        print("Check " + path)

def handle_dir(path, word):
    senlist = []
    filelist = get_filelist(path)
    for item in filelist:
        senlist += handle_txt(path + '/', item, word)
    return senlist

def handle_txt(path, filename, word):
    f = open(path + filename, 'r')
    index = 0
    senlist = []
    line = f.readline()
    while line:
        if word in line:
            line += '(' + filename + ', ' + (str)(index) + ')'
            senlist.append(line)
        line = f.readline()
        index += 1
    f.close()
    return senlist

def dig_main(word):
    senlist = []
    path = 'txt'
    dirlist = get_filelist(path);
    for item in dirlist:
        senlist += handle_dir(path + '/' + item, word)
    print_sentence(word, senlist)

if (len(argv) == 2):
    word = argv[1]
else:
    word = input('word: ')
dig_main(word)

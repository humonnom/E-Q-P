import os
from sys import argv
import docx2txt
import glob

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

def handle_dir(path, word, senlist):
    filelist = get_filelist(path)
    for item in filelist:
        senlist = handle_txt(path + '/', item, word, senlist)
    return (senlist)

def docx_to_txt(path, filename):
    text = docx2txt.process(path + filename).split('\n')
    newfile = os.path.splitext(filename)[0] + '.txt'
    f = open(path + newfile, 'w')
    for item in text:
        f.write(item + '\n')
    f.close()
    os.remove(path + filename)
    return (newfile)

def handle_txt(path, filename, word, senlist):
    ext = os.path.splitext(filename)[-1]
    if ext == '.docx':
        filename = docx_to_txt(path, filename)
    f = open(path + filename, 'r')
    index = 0
    line = f.readline()
    while line:
        if word in line:
            line += '(' + filename + ', ' + (str)(index) + ')'
            senlist.append(line)
        line = f.readline()
        index += 1
    f.close()
    return (senlist)

def dig_main(word):
    senlist = []
    path = 'txt'
    dirlist = get_filelist(path);
    for item in dirlist:
        senlist = handle_dir(path + '/' + item, word, senlist)
#    print_sentence(word, senlist)

if (len(argv) == 2):
    word = argv[1]
else:
    word = input('word: ')
dig_main(word)

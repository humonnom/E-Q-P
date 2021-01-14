from sys import argv
import digging_sub as d

if (len(argv) == 2):
    word = argv[1]
else:
    word = input('word: ')

path = d.dig_main(word, "print")
print("Created : ", path)

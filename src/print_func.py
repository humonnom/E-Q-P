# class
class color:
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

class info:
    length = 50

def _center(s, *args):
    if (len(args) == 0):
        print(s.center(info.length))
    else:
        print(s.center(info.length, args[0]))

def _left(s, *args):
    if (len(args) == 0):
        print(s.ljust(info.length))
    else:
        print(s.ljust(info.length, args[0]))

def _right(s, *args):
    if (len(args) == 0):
        print(s.rjust(info.length))
    else:
        print(s.rjust(info.length, args[0]))

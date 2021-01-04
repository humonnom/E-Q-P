import func as ft
import print_func as p

# print
def print_header(title):
    ft.clear()
    title = ' ' + title + ' '
    p._center("#"*50)
    p._center(title, '#')
    p._center("#"*50)
    p._left('(q:quit)')

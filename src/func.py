import pandas as pd
import numpy as np
import os
from IPython.display import display
import time
from datetime import datetime, timedelta

import print_func as p

# class
class color:
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

class info:
    length = 50

# function
def clear():
    os.system('clear')

def exit(data):
    if (data == 'q'):
        print("Are you sure?(y/n)".center(info.length))
        check = input("\t\t: ")
        if (check == 'y'):
            os._exit(1)

def select_range():
    print(color.BOLD + "----Select a course----".center(info.length) + color.END)
    print("1. Review last week".center(info.length))
    print("2. Review this week".center(info.length))
    print("3. Review today(default)".center(info.length))
    print(color.BOLD + "-----------------------".center(info.length) + color.END)
    _range = input("\t\t: ")
    exit(_range) 
    time.sleep(0.3)
    s = "You have selected " + str(_range)
    print(s.center(info.length))
    return _range

def print_result(df_result):
    your_score = df_result['Score'].sum()
    whole_score = len(df_result)
    s = "Your score is " + (str)(your_score) + "/" + (str)(whole_score)
    print(color.BOLD + s.center(info.length) + color.END)
    print('\n')
    pd.set_option('display.max_columns', 10)
    display(df_result)
    print("\n -> If you want more, run", color.BOLD + "./review.sh" + color.END, "file")

def grade(index, df_result, test_range, df_answer, means):
    answer = input("\t\tanswer: ")
    exit(answer)
    if (answer == df_answer.iloc[index, 0]):
        score = 1
    else :
        score = 0
    df_result = df_result.append(pd.DataFrame([[index, answer, df_answer.iloc[index, 0], score, means]], columns=['Num', 'Yours', 'Answer','Score', 'Means']), ignore_index=True)
    return (df_result)

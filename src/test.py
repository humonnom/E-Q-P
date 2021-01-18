import pandas as pd
import numpy as np
import os
from IPython.display import display
import time
from datetime import datetime, timedelta
from test_range import get_test_range
import header
from sys import argv

import print_func as p
import func as ft

def print_quiz(index, value):
    print(color.BOLD + 'Quiz num ', index)
    print(color.END)
    print(value.sentence)
    if (value.essay == 0):
        print(color.UNDERLINE + '(' + value.means + ')' + color.END)
        print(value.hint)
    print('\n')
    return(ft.grade(index, df_result, test_range, df_answer, value.means))

# get info
color = ft.color()
info = ft.info()

# print header
header.print_header("TEST")

# dataframe
df = pd.read_csv("quiz.csv")
df = df.iloc[:,:7]
df.columns=['date', 'name', 'chapter', 'sentence', 'means', 'hint', 'essay']
df_answer = pd.read_csv("answer.csv")
df_answer = df_answer.iloc[:, 2:3]

# set test range
test_range = get_test_range(df, argv)
if (type(test_range) == list):
    flag_whole = 1
else:
    flag_whole = 0
# remove essay questions
# test_range = test_range[test_range.essay == 0]

# create dataframe
df_result = pd.DataFrame(columns=['Num', 'Yours', 'Answer','Score', 'Means'])

# print quiz
if (flag_whole):
    for index in test_range:
        df_result = print_quiz(index, df.iloc[index])
else:
    for row_index, value in test_range.iterrows():
        df_result = print_quiz(row_index, value)

ft.clear()
df_result.set_index('Num', inplace=True)
df_result.to_csv("result.csv", mode='w')
ft.print_result(df_result)

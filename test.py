import pandas as pd
import numpy as np
import os
import time
from datetime import datetime, timedelta
from IPython.display import display

# functions
def ft_exit(data):
    if (data == 'q'):
        print("Are you sure?(y/n)".center(length))
        check = input("\t\t: ")
        if (check == 'y'):
            os._exit(1)

def ft_select_range():
    print(color.BOLD + "----Select a course----".center(length) + color.END)
    print("1. Review last week".center(length))
    print("2. Review this week".center(length))
    print("3. Review today(default)".center(length))
    print(color.BOLD + "-----------------------".center(length) + color.END)
    test_range = input("\t\t: ")
    ft_exit(test_range) 
    time.sleep(1)
    s = "You have selected " + str(test_range)
    print(s.center(length))
    return test_range

def ft_print_result(df_result):
    your_score = df_result['Score'].sum()
    whole_score = len(df_result)
    s = "Your score is " + (str)(your_score) + "/" + (str)(whole_score)
    print(color.BOLD + s.center(length) + color.END)
    print('\n')
    display(df_result)

def ft_grade(index, df_result, test_range, df_answer):
    answer = input("\t\tanswer: ")
    ft_exit(answer)
    if (answer == df_answer.iloc[index, 0]):
        score = 1
    else :
        score = 0
    df_result = df_result.append(pd.DataFrame([[index, answer, df_answer.iloc[index, 0], score]], columns=['Num', 'Yours', 'Right answer', 'Score']), ignore_index=True)
    return (df_result)

length = 50
class color:
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

# print
print(("#"*50).center(length))
print(" TEST ".center(length, '#'))
print(("#"*50).center(length))
print('(q:quit)')

# dataframe
df = pd.read_csv('quiz.csv')
df = df.iloc[:,:7]
df.columns=['date', 'name', 'chapter', 'sentence', 'means', 'words', 'essay']
df_answer = pd.read_csv('answer.csv')
df_answer = df_answer.iloc[:, 2:3]

## set test range
test_range = ft_select_range()
today = datetime.now()
weekday = datetime.today().weekday()
start = today
end = today
if (test_range == '1'):
    start = today - timedelta(days=(weekday + 7))
    end = start + timedelta(days=5)
if (test_range == '2'):
    start = today - timedelta(days=weekday)
    end = today
delta = end - start
datelist = []
for i in range(delta.days + 1):
    day = (start + timedelta(days=i)).strftime("%Y-%m-%d")
    datelist.append(day)
time.sleep(1)
s = "Test: " + datelist[0] + ' ~ ' + datelist[-1]
time.sleep(1)
print(s.center(length))
# set date range
is_test_range = df['date'].isin(datelist)
test_range = df[is_test_range]

# remove essay questions
test_range = test_range[test_range.essay == 0]

# create dataframe
df_result = pd.DataFrame(columns=['Num', 'Yours', 'Right answer', 'Score'])


# print quiz
for row_index, value in test_range.iterrows():
    print(color.BOLD + 'Quiz num ', row_index)
    print(color.END)
    print(value.sentence)
    print(color.UNDERLINE + '(' + value.means + ')' + color.END)
    df_result = ft_grade(row_index, df_result, test_range, df_answer)
    print('\n')

df_result.set_index('Num', inplace=True)

ft_print_result(df_result)

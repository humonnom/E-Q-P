import pandas as pd
import numpy as np
import os
import time
from datetime import datetime, timedelta

import func as ft

# get info
color = ft.color()
info = ft.info()

def get_test_range(df, argv):
    if (len(argv) == 2 and argv[1] == 're'):
        test_range = get_retest_range(df)
    else :
        test_range = get_date_range(df, argv)
    
    # empty test range ? -> end test
    # print
    return (test_range)

def get_retest_range(df):
    df_re = pd.read_csv("result.csv")
    df_re = df_re[df_re.Score == 0]
    testlist = df_re['Num'].to_list()
    df = df.iloc[testlist, :]
    print_range(testlist)
    return(df)

def get_date_range(df, argv):
    today = datetime.now()
    weekday = datetime.today().weekday()
    testlist = []
    if (len(argv) > 1):
        script, day = argv
        testlist.append(day)
    else:
        _range = ft.select_range()
        start = today
        end = today
        if (_range == '1'):
            start = today - timedelta(days=(weekday + 7))
            end = start + timedelta(days=5)
        if (_range == '2'):
            start = today - timedelta(days=weekday)
            end = today
        delta = end - start
        for i in range(delta.days + 1):
            day = (start + timedelta(days=i)).strftime("%Y-%m-%d")
            testlist.append(day)
    print_range(testlist)
    is_test_range = df['date'].isin(testlist)
    return(df[is_test_range])

def print_range(testlist):
    time.sleep(0.3)
    s = "Test: " + (str)(testlist[0]) + ' ~ ' + (str)(testlist[-1])
    time.sleep(0.3)
    print(s.center(info.length))

import pandas as pd
import numpy as np
import os
import time
from datetime import datetime, timedelta
from IPython.display import display

import dig_main from digging 
import header
import print_func as p

def get_file():
    df = pd.read_csv("result.csv", index_col=0)
    pd.set_option('display.max_columns', 10)
    df.replace(np.nan, " ", inplace=True)
    display(df)
    return (df)

def get_examples(wordlist):
    for index, row in wordlist.iterrows():
        print("=" * 7, index, "=" * 7)
        sentence = get_sentence(row[0])
        print(sentence)
        print("=" * 19)

header.print_header("Review")
df = get_file()
wordlist =  df.loc[:, ['Answer']]
p._left(" -> If you want to see the examples, press 'y'")
more = input()
if (more == 'n'):
    exit(1)
else:
    p._left(" -> Creating example file")
    get_examples(wordlist)
    p._left(" -> Check the dst folder")

import pandas as pd
import numpy as np
import os
import time
from datetime import datetime, timedelta
from IPython.display import display

import header
import print_func as p

def get_file():
    df_result = pd.read_csv("result.csv", index_col=0)
    pd.set_option('display.max_columns', 10)
    df_result.replace(np.nan, " ", inplace=True)
    display(df_result)
    return (df_result)

def get_examples(wordlist):
    print(wordlist)

header.print_header("Review")
wordlist = get_file()
p._left(" -> If you want to see the examples, press 'y'")
more = input()
if (more == 'n'):
    exit(1)
else:
    p._left(" -> Creating example file")
    get_examples(wordlist)
    p._left(" -> Check the dst folder")

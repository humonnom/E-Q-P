#!/bin/bash

echo "Check version"
python3 --version
IPython --version
pip --version

pip list | grep pandas
# pip install pandas
pip list | grep numpy
# pip install numpy

key="1TBUUlKuqtuZQitLD-chcIbDubWww8IH0DQtnBeIPTvc"
sheet_name="Blank Quiz"

wget --no-check-certificate "https://docs.google.com/spreadsheets/d/${key}/gviz/tq?tqx=out:csv&sheet=${sheet_name}" -O quiz.csv

wget --no-check-certificate "https://docs.google.com/spreadsheets/d/${key}/gviz/tq?tqx=out:csv&sheet=${sheet_name}&gid=209686043" -O answer.csv

echo "exicute python file"

python3 test.py

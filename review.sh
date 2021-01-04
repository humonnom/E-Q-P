#!/bin/bash

echo "Create result file"
cd src
python3 review.py
cd ../
echo "result file: src/result.csv"

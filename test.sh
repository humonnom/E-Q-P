#!/bin/bash

echo "Start Test"
cd src
if [ $# -eq 1 ]
then
	python3 test.py "$1"
else	
	python3 test.py
fi
cd ..
echo "review: ./review.sh"

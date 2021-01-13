#!/bin/bash

echo "Searching Program"
cd src
if [ $# -eq 1 ]
then
	python3 digging.py "$1"
else	
	python3 digging.py
fi

echo "File location -> src/Diglett"

cd ..

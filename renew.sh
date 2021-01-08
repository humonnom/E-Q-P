#!/bin/bash

location=""

function check_install()
{
	python3 --version
	IPython --version
	pip --version
	pip list | grep pandas
	# pip install pandas
	pip list | grep numpy
	# pip install numpy
}

function get_google()
{
	key="1TBUUlKuqtuZQitLD-chcIbDubWww8IH0DQtnBeIPTvc"
	sheet_name="Blank Quiz"
	wget --no-check-certificate "https://docs.google.com/spreadsheets/d/${key}/gviz/tq?tqx=out:csv&sheet=${sheet_name}" -O quiz.csv
	wget --no-check-certificate "https://docs.google.com/spreadsheets/d/${key}/gviz/tq?tqx=out:csv&sheet=${sheet_name}&gid=209686043" -O answer.csv
}

function get_custom()
{
	echo "You will be test on {$1}"
	location=`find src/txt/* -name "$1.txt"`
	if [ -z $location ];then
		echo "There is no file named '$1'"
		echo "--> Deactivate EQP"
		exit 0
	fi
}

echo "1. Check version"
check_install
echo "2. Get quiz.csv & answer.csv"
if [ $# -eq 1 ];then
	get_custom $1
else	
	get_google
fi
mv quiz.csv src/
mv answer.csv src/
echo "3. Done"
echo "run test: ./test.sh"


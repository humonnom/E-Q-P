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
	key="1xUuN0pHPYingmQiarXT6sLgfEErOaC1LH2mpOo6LfRI"
	sheet_name="Blank Quiz"
	wget --no-check-certificate "https://docs.google.com/spreadsheets/d/${key}/gviz/tq?tqx=out:csv&sheet=${sheet_name}" -O quiz.csv
	wget --no-check-certificate "https://docs.google.com/spreadsheets/d/${key}/gviz/tq?tqx=out:csv&sheet=${sheet_name}&gid=209686043" -O answer.csv
#	echo "You will be test on {$1}"
#	location=`find src/txt/* -name "$1.txt"`
#	if [ -z $location ];then
#		echo "There is no file named '$1'"
#		echo "--> Deactivate EQP"
#		exit 0
#	fi
}

function change_to_txt()
{
	cd src
	./chtxt.sh
	cd ..
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
echo "3. Change srt file -> txt file"
change_to_txt
echo "4. Done"
echo "run test: ./test.sh"


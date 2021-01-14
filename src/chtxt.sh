#!/bin/sh
cd txt/
dir_array=`ls`
for item in ${dir_array};do
	cd ${item}
	for file in *.srt;do
		mv "${file}" "${file%%srt}txt"
	done
	cd ../
done
cd ../

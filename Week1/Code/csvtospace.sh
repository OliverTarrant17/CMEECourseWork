#! /bin/bash
# Author: Oliver Tarrant oit16@imperial.ac.uk
# Script: csvtospace.sh
# Desc: substitute the commas in the files with space
# 	saves the output as filename_sapce
# Arguments: 1 -> comma delimited file
# Date Oct 2017

echo "Creating a comma delimited version of $1 ..."

cat $1 | tr -s "," " "  >> $1_space

echo "Done!"

exit

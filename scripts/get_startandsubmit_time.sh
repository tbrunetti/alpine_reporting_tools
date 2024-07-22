#!/bin/bash

output=$(sacct --allusers --starttime=05/01/24 --endtime=05/02/24 -X --format
=JobID,Account,start,submit | grep -i amc)

# echo output

# Extract start and submit times
echo "$output" | awk '{print $3,$4}' # > output.csv # test first

# FUTURE: Call python script that calculates the difference between start and submit:
# example.py


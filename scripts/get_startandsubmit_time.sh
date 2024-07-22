#!/bin/bash

output=$(sacct --allusers --starttime=05/01/24 --endtime=05/02/24 -X --format=JobID,Account,start,submit | grep $

# echo output

# Extract start and submit times
echo "$output" | awk '{print $3,$4}' > submitstart.csv


# FUTURE: potentially call ml anaconda and conda env
# FUTURE: Call python script that calculates the difference between start and submit:
python queue_time_calc.py

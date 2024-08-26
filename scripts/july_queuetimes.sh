#!/bin/bash

output=$(sacct --allusers --starttime=07/01/24 --endtime=07/31/24 -X --format=JobID,Account,start,submit | grep -i amc)

# echo output

# Extract start and submit times
echo "$output" | awk '{print $3,$4}' > submitstart.csv # test first

# FUTURE: potentially call ml anaconda and conda env
ml anaconda
# FUTURE: Call python script that calculates the difference between start and submit:
##python old_queue_time_calc.py
python queue_time_calc.py

python monthly_stats.py
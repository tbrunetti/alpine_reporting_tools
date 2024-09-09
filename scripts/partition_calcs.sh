#!/bin/bash


# Check if a partition argument is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <partition>"
  exit 1
fi

PARTITION="$1"

output=$(sacct --allusers --starttime=01/01/24 --endtime=09/01/24 -X --partition=$PARTITION --format=JobID,Account,start,submit,partition | grep -i amc)

# COMMENT OUT LATER:
#echo output

# Extract start and submit times

echo "$output" > results/$PARTITION.csv

echo "$output" | awk '{print $3,$4}' > submitstart.csv

ml anaconda

python queue_time_calc.py

python partition.py

rm -f queue_time_perjob.csv
rm -f submitstart.csv

mv monthly_statistics.csv "${PARTITION}_stats.csv"

mv box_plot_JantoSept1_partition.png "${PARTITION}_boxplot_JantoAug31.png"
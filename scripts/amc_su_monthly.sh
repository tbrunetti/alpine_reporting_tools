#!/bin/bash

output=$(sreport -t hours -T billing -P cluster AccountUtilizationByUser \
        start=2024-01-01 end=2024-02-01 tree account=amc-general)

#echo "$output"

# Extract user names and save to output.txt
#echo "$output" | awk '{print $3}' > output.txt

# Process output to extract numbers and calculate total
echo "$output" | awk '{print $NF}' | grep -Eo '[0-9]+' | awk '{sum += $1} END {print "Total Monthly
 SUs used by AMC Users: ", sum}'

#!/bin/bash

output=$(sreport -t hours -T billing -P cluster AccountUtilizationByUser \
        start=2024-01-01 end=2024-02-01 tree account=amc-general)

#echo "$output"

# Extract user names and save to output.txt
#echo "$output" | awk '{print $3}' > output.txt

# Process output to extract numbers and calculate total
echo "$output" | awk '{print $NF}' | grep -Eo '[0-9]+' | awk '{sum += $1} END {print "Total Monthly
 SUs used by AMC Users: ", sum}'



#result=$(echo "$output" | awk '{gsub(/\|billing\|/, " "); print $3, $5; sum += $5} END {print "Tot
al: ", sum}')
#result=$(echo "$output" | awk '{print $3, gensub(/.*\|/, "", "g", $6); sum += gensub(/.*\|/, "", "
g", $6)} END {print "Total: ", sum}')
# Print the results for 1 month out, keeping only the name and SUs used. Also make it print a sum t
otal
#result=$(echo "$output" | awk '{print $3, substr($6, index($6, "|")+1); sum += substr($5, index($5
, "|")+1)} END {print "Total Monthly SUs: ", sum}')

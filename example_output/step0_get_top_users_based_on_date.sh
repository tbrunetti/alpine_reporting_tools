#!/bin/bash

echo "###########Generates dates###########"

python get_dates.py

echo "###########Retrieving Start and end date###########"
START_DATE=`sed -n 1p dates.txt`
END_DATE=`sed -n 2p dates.txt`
echo "###########Start date is ${START_DATE}###########"
echo "###########End date is ${END_DATE}###########"



echo "###########Reporting top users based on dates ###########"
sreport user topusage -P start=$START_DATE  end=$END_DATE  -t percent account=amc-general > cut.txt

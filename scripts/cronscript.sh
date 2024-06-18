#!/bin/bash

TODAY=`echo $(date +%Y-%m-%d)`
YEAR=`echo $(date +%Y)`
MONTH=`echo ${TODAY: 5:2}`
DAY=`echo ${TODAY: 8}`
DAY_week_ago=`echo $(( ${DAY} - 7))`

if [[ "$DAY_week_Ago" -lt 0 ]]
then
    previousMonth=$(printf "%02d" $(( ($MONTH-1) % 12 )) )
    lastdaypreviousMonthlastdaypreviousMonth=`echo $(date -d "$(date +%Y-%m-01) -1 day" +%Y%m%d)`
    abs_val=`echo $DAY_week_ago: 1}`
    Format_day_week_ago="$(($lastdaypreviousMonthlastdaypreviousMonth+1-$abs_val))"
else
    Format_day_week_ago=$DAY_week_ago	
    previousMonth=$MONTH
fi

0 4 * * 1-5 /projects/kfotso@xsede.org/slurm_report/June_2024_/alpine_reporting_tools/scripts/scrape_user_metrics.sh USERS=brunetti@xsede.org,kfotso@xsede.org,msherren@xsede.org START_DATE=$YEAR-$previousMonth-$Format_day_week_ago END_DATE=$TODAY

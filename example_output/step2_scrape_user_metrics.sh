#!/bin/bash

echo "###########Retrieving top 5 users###########"
top1=`sed -n 1p top_users.txt`
top2=`sed -n 2p top_users.txt`
top3=`sed -n 3p top_users.txt`
top4=`sed -n 4p top_users.txt`
top5=`sed -n 5p top_users.txt`

echo "###########Top 5 users are###########"
echo $top1
echo $top2
echo $top3
echo $top4
echo $top5

echo "###########Retrieving Start and end date###########"
START_DATE=`sed -n 1p dates.txt`
END_DATE=`sed -n 2p dates.txt`


echo "###########Start date is ${START_DATE}###########"
echo "###########End date is ${END_DATE}###########"

echo "###########Calculate levelfs###########"
/projects/kfotso@xsede.org/slurm_report/June_2024_/alpine_reporting_tools/scripts/calc_levelfs.sh USERS=$top1,$top2,$top3,$top4,$top5 START_DATE=$START_DATE END_DATE=$END_DATE


echo "###########Calculate SUs###########"
/projects/kfotso@xsede.org/slurm_report/June_2024_/alpine_reporting_tools/scripts/calc_SUs.sh USERS=$top1,$top2,$top3,$top4,$top5 START_DATE=$START_DATE END_DATE=$END_DATE


echo "###########Save as dataframe and plot###########"
python /projects/kfotso@xsede.org/slurm_report/June_2024_/alpine_reporting_tools/scripts/plot_levelfs_SU.py
#/projects/kfotso@xsede.org/slurm_report/June_2024_/alpine_reporting_tools/scripts/scrape_user_metrics.sh USERS=$top1,$top2,$top3,$top4,$top5 START_DATE=$START_DATE END_DATE=$END_DATE

echo "###########Saving the jobs efficiency###########"
bash /projects/kfotso@xsede.org/slurm_report/June_2024_/alpine_reporting_tools/scripts/calc_eff_.sh USERS=$top1,$top2,$top3,$top4,$top5 START_DATE=$START_DATE END_DATE=$END_DATE

echo "###########Parsing txt file, making dataframe, saving and plotting###########"
python /projects/kfotso@xsede.org/slurm_report/June_2024_/alpine_reporting_tools/scripts/parse_eff_+_df.py


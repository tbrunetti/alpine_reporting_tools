#!/bin/bash  

module load slurmtools  

# parse input arguments
for ARGS in "$@";
do
    PARAM=$(echo $ARGS | cut -f1 -d=) # delimiter is = sign w/o spaces
    PARAM_LEN=${#PARAM} # counts length of argument, since the value will be the next character after this since delim on =
    echo "${PARAM_LEN}"
    VALUE="${ARGS:$PARAM_LEN+1}"
    echo "${VALUE}"
    export "${PARAM}"="${VALUE}" # set the keyword arg to the value specified at runtime
done

# print out all input parameters and their values
echo "USERS = ${USERS}" # list of users should be comma separated
echo "START_DATE = ${START_DATE}"
echo "END_DATE = ${END_DATE}"

# make output file
DATE_GEN=$( date +"%m%d%Y" )
OUTFILE="data_scrape_by_user_dates_START="${START_DATE}"_END="${END_DATE}"_reportGeneratedOn_"${DATE_GEN}".txt"
touch ${OUTFILE}

# get all users
ALL_USERS=( $(echo ${USERS} | sed 's/,/ /g') )

for username in ${ALL_USERS[@]};
do
	echo "Gathering users statistics for: ${username}"
        echo "NEW USER: ${username}" >> ${OUTFILE}
	# report the total number of jobs submitted that request x number of CPU resources
	echo "JOBSIZE" >> ${OUTFILE}
	sreport job sizesbyaccount alpine users=${username} account=amc-general PrintJobCount --parsable START=${START_DATE} END=${END_DATE} | sed -n '5,6p' >> ${OUTFILE}
	# report the total number of SUs consumed by each user
	echo "SU" >> ${OUTFILE}
	sreport  -t hours -T billing -P cluster AccountUtilizationByUser users=${username} start=${START_DATE} end=${END_DATE} tree acct=amc-general | sed -n '5,6p' >> ${OUTFILE}
	# get total jobs ran and their status
	echo "TOTALJOBS" >> ${OUTFILE}
	sacct --uid ${username} -t -S${START_DATE} -E${END_DATE} --state COMPLETED,FAILED,TIMEOUT,OOM --parsable --noheader | awk -F"|" '{print $1}' | sort | uniq | wc -l >> ${OUTFILE}
	echo "JOBSTATUS" >> ${OUTFILE}
	sacct --uid ${username} -t -S${START_DATE} -E${END_DATE} --state COMPLETED,FAILED,TIMEOUT,OOM --parsable --noheader | awk -F"|" '{print $6}' | sort |  uniq -c | awk '{print $2"\t"$1}' >> ${OUTFILE}
	# seff statistics for each users' jobs  
	echo "SEFF" >> ${OUTFILE}
	ALL_JOB_IDS=( $( sacct --uid ${username} -t -S${START_DATE} -E${END_DATE} --state COMPLETED,FAILED,TIMEOUT,OOM --parsable --noheader | awk -F"|" '{print $1}' | sort | uniq ))
	for job in ${ALL_JOB_IDS[@]};
	do
		seff ${job} >> ${OUTFILE}
	done
	echo "LEVELFS" >> ${OUTFILE}
	levelfs ${username} | tail -n+6 >> ${OUTFILE}
done

paste <(echo "REPORT FINISHED ON" ) <(date)

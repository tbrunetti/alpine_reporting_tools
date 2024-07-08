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
	echo "NEW USER: ${username}" >> levelfs_${END_DATE}.txt
	echo "LEVELFS" >> levelfs_${END_DATE}.txt
	levelfs ${username} | tail -n+6 >> levelfs_${END_DATE}.txt
done

paste <(echo "REPORT FINISHED ON" ) <(date)

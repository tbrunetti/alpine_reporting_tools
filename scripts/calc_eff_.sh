
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
OUTFILE="Eff_Raw_data.txt"

if [ -f "$OUTFILE" ] ; then
    rm "$OUTFILE"
fi

touch ${OUTFILE}
# get all users
ALL_USERS=( $(echo ${USERS} | sed 's/,/ /g') )
for username in ${ALL_USERS[@]};
do
        echo "Gathering users statistics for: ${username}"
        ALL_JOB_IDS=( $( sacct --uid ${username} -t -S${START_DATE} -E${END_DATE} --state COMPLETED,FAILED,TIMEOUT,OOM --parsable --noheader | awk -F"|" '{print $1}' | sort | uniq ))
	for job in ${ALL_JOB_IDS[@]};
        do
                seff ${job} >> ${OUTFILE}
        done
done
paste <(echo "REPORT FINISHED ON" ) <(date)

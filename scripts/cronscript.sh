#!/bin/bash

0 4 * * 1-5 /projects/kfotso@xsede.org/slurm_report/June_2024_/alpine_reporting_tools/scripts/actual_script USERS=brunetti@xsede.org,kfotso@xsede.org,msherren@xsede.org START_DATE=$YEAR-$previousMonth-$Format_day_week_ago END_DATE=$TODAY

#!/bin/bash

# Get a list of active users from your organization
active_users=$(sacctmgr -P show user | grep -i amc-general | awk -F'|' '{print $1}')

echo $active_users

start_date="2024-07-01"

echo "Users active since $start_date:"
sacct -S $start_date --format=User | sort | uniq | while read user; do
    if echo "$active_users" | grep -q "^$user$"; then
        echo $user
    fi
done

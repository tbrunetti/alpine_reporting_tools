# alpine_reporting_tools
A repo to contain information, scripts, and ideas of different ways to report user, departmental, and instiutional usage on Alpine

## Usage  
The following command would scrape metrics for brunetti, kfotso, and msherren username between the months of May 1, 2024 through May 31, 2024.  For example results, see [example_output_folder](https://github.com/tbrunetti/alpine_reporting_tools/tree/main/example_output)  

```
acompile
./scrape_user_metrics.sh USERS=brunetti@xsede.org,kfotso@xsede.org,msherren@xsede.org START_DATE=2024-05-01 END_DATE=2024-05-31
```


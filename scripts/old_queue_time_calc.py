import csv
from datetime import datetime

# Function separates datetime string into datetime object
def separate_datetime(dt_str):
    return datetime.fromisoformat(dt_str.strip())

# Function calculates time difference
def calculate_time_difference(dt1, dt2):
    return dt2 - dt1

# Input and output
input_filename = 'submitstart.csv'
output_filename = 'queue_time_perjob.csv'

# Reads input CSV file, calculates, writes to output
with open(input_filename, 'r') as infile, open(output_filename, 'w', newline='') as outfile:
    reader = csv.reader(infile, delimiter=' ')
    writer = csv.writer(outfile)
    
    for row in reader:
        if len(row) != 2:
            continue
        
        datetime1_str, datetime2_str = row
        
        # Separate datetime strings into datetime objects
        datetime1 = separate_datetime(datetime1_str)
        datetime2 = separate_datetime(datetime2_str)
        
        # Calculate time difference
        time_diff = calculate_time_difference(datetime1, datetime2)
        
        # Write results to output CSV
        writer.writerow([datetime1_str, datetime2_str, str(time_diff)])

# TEST
print(datetime1_str, " ", datetime2_str, " ", str(time_diff))

#print(f"Output saved to queue_times_perjob.csv")

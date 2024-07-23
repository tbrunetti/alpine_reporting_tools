import csv
from datetime import datetime

# separate date/time string into date/time object:
def parse_datetime(datetime_str):
        return datetime.fromisoformat(datetime_str)
# Calculate time difference in seconds:
def calculate_time_difference(start_time, submit_time):
        diff = submit_time - start_time
        return diff.total_seconds()

# Main function to read and calculate:
def calculate_differences(csv_file, output_file):
        with open(csv_file, newline='') as csvfile, open(output_file, 'w', newline='') as outfile:
                reader = csv.reader(csvfile, delimiter=' ')
                writer = csv.writer(outfile)
                writer.writerow(['Start Time', 'Submit Time', 'Difference (seconds)'])  # Write he$

                for row in reader:
                        if len(row) < 2:
                                continue
                        start_time_str, submit_time_str = row[0], row[1]
                        # Sanity check:
                        # print(f"Start Time String: {start_time_str}")
                        # print(f"Submit Time String: {submit_time_str}")
                        
                # Skip rows with "None":
                        if start_time_str == "None" or submit_time_str == "None":
                                continue
                        
                        try:
                                start_time = parse_datetime(start_time_str)
                                submit_time = parse_datetime(submit_time_str)
                        except ValueError:
                                continue        # skip rows where date/time strings are "None"

                        time_difference = (submit_time - start_time).total_seconds()
                  
                        # print(f"Start Time: {start_time} | Submit Time: {submit_time} | Difference$
                        writer.writerow([start_time, submit_time, time_difference])

# Using data submitstart.csv as input
if __name__ == "__main__":
        input_csv = 'submitstart.csv'
        output_csv = 'queue_time_perjob.csv'
        calculate_differences(input_csv, output_csv)

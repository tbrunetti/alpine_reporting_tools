import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
file = 'queue_time_perjob.csv'
df = pd.read_csv(file)

## !!! DELETE IF NOT NECESSARY... Already in datetime format?

# Convert 'Start Time' and 'Submit Time' to datetime format
df['Start Time'] = pd.to_datetime(df['Start Time'])
df['Submit Time'] = pd.to_datetime(df['Submit Time'])

# Extract the day from the 'Start Time' for grouping
df['Day'] = df['Start Time'].dt.day

average_diff_per_day = df.groupby('Day')['Difference (min)'].mean()

# Sort the average difference per day by day
sorted_avg_diff_per_day = average_diff_per_day.sort_index()

# Print the sorted average difference per day
print("Average 'Difference (min)' per day in June (sorted by day):")
print(sorted_avg_diff_per_day)

sorted_avg_diff_per_day.to_csv('average_difference_per_day_july.csv', header=True)



# Remove outliers:
filtered_df = df[df['Difference (min)'] <= 50]

# Boxplot of July chart:

# Box plot for 'Difference (min)'
plt.boxplot(filtered_df['Difference (min)'], vert=False, patch_artist=True)
plt.title('Box Plot of Difference (min) for June')
plt.xlabel('Difference (min)')
plt.grid(True)

# Save the plot to a PNG file
plt.savefig('box_plot_difference_trimmed_outliers_july.png')

# Optionally, with a PDF
# plt.savefig('box_plot_difference_min_july.pdf')

# Close the plot to free up memory
plt.close()



# Create statistics file for output to compare to boxplot:

df['Month'] = df['Start Time'].dt.month

# Sanity check!
print(df)

july_df = df[df['Month'] == 7]  # Check with sanity check!!

q1 = july_df['Difference (min)'].quantile(0.25)
median = july_df['Difference (min)'].median()
q3 = july_df['Difference (min)'].quantile(0.75)
mean = july_df['Difference (min)'].mean()
min_val = july_df['Difference (min)'].min()
max_val = july_df['Difference (min)'].max()

# Create a DataFrame with the statistics
stats_df = pd.DataFrame({
    'Statistic': ['Q1', 'Median (Q2)', 'Q3', 'Mean', 'Min', 'Max'],
    'Value': [q1, median, q3, mean, min_val, max_val]
})

# Save the statistics to a new CSV file
stats_df.to_csv('july_queue_time_statistics.csv', index=False)
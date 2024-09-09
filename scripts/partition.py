import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
file = 'queue_time_perjob.csv'
df = pd.read_csv(file)

# Convert, Group, and sort:
df['Start Time'] = pd.to_datetime(df['Start Time'])
df['Submit Time'] = pd.to_datetime(df['Submit Time'])

df['Day'] = df['Start Time'].dt.day

average_diff_per_day = df.groupby('Day')['Difference (min)'].mean()

sorted_avg_diff_per_day = average_diff_per_day.sort_index()

sorted_avg_diff_per_day.to_csv('average_difference_per_day.csv', header=True)

# Remove outliers:
filtered_df = df[df['Difference (min)'] <= 10000]


# Boxplot of partition chart:

plt.boxplot(filtered_df['Difference (min)'], vert=False, patch_artist=True)
plt.title('Box Plot of Difference (min) for Partition:')
plt.xlabel('Difference (min)')
plt.grid(True)

# Save the plot to a PNG file
plt.savefig('box_plot_JantoSept1_partition.png')

# Save to a PDF
# plt.savefig('box_plot_JantoSept1_partition.pdf')

plt.close()


# Create statistics file for output to compare to boxplot:

df['Month'] = df['Start Time'].dt.month
df = df[df['Month'].isin(range(1, 10))]


months = df['Month'].unique()

# Dictionary to hold each month:
stats_dict = {}

for month in months:
    # Filter the df month by month:
    monthly_df = df[df['Month'] == month]
    
    # Compute:
    q1 = monthly_df['Difference (min)'].quantile(0.25)
    median = monthly_df['Difference (min)'].median()
    q3 = monthly_df['Difference (min)'].quantile(0.75)
    mean = monthly_df['Difference (min)'].mean()
    min_val = monthly_df['Difference (min)'].min()
    max_val = monthly_df['Difference (min)'].max()
    total = len(monthly_df)
    
    # Store statistics in the dictionary
    stats_dict[month] = [q1, median, q3, mean, min_val, max_val, total]

# Create new dataframe with statistics:
stats_df = pd.DataFrame(stats_dict, index=['Q1', 'Median (Q2)', 'Q3', 'Mean', 'Min', 'Max', 'Total'])

# Transpose the dataframe:
stats_df = stats_df.T

stats_df['Month'] = stats_df.index

stats_df = stats_df[['Month', 'Q1', 'Median (Q2)', 'Q3', 'Mean', 'Min', 'Max', 'Total']]

# Save statistics:
stats_df.to_csv('monthly_statistics.csv', index=False)
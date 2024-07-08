# Parsing top users 
import pandas as pd
import os

print(f"********Parsing top users********\n")
df = pd.read_csv("cut.txt", sep="|", skiprows=5, names=["Cluster", "Login", "Proper Name", "Account", "Used", "Energy"])
top_users = df['Login'][:5].values.tolist()

print(f"********Saving them into text file********\n")
with open("top_users.txt", "w") as output:
    for row in top_users:
        output.write(str(row) + '\n')
        
        
# Getting the dates
from datetime import datetime
import datetime as DT

today_formatted = datetime.today().strftime('%Y-%m-%d')
print(f"********Today's date is {today_formatted}********\n")

today = DT.date.today()
week_ago = today - DT.timedelta(days=7)
week_ago_formatted = week_ago.strftime('%Y-%m-%d')
print(f"********Date 7 days ago is {week_ago_formatted}********\n")


print(f"********Saving dates into file dates.txt ********\n")
with open("dates.txt", "w") as output:
    output.write(str(week_ago_formatted) + '\n')
    output.write(str(today_formatted) + '\n')
    



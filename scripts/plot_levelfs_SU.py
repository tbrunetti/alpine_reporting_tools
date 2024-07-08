import re
from datetime import datetime
import datetime as DT
import pandas as pd
today_formatted = datetime.today().strftime('%Y-%m-%d')

# Levelfs textfile
print(f"********Parsing and Saving levelfs as dataframe********\n")

levelfs=f"levelfs_{today_formatted}.txt"
with open(levelfs, 'r') as f:
    data = f.readlines()
    
#d = {'User': [], 'User_levelfs': [], 'Inst_levelfs': [], }
d = {'User_levelfs': [], 'Inst_levelfs': [], } 
index = []
for line in data: # go through file line by line      
    if line.startswith('NEW USER'): #or line != 'LEVELFS\n': # skip new line characters
        line = line.replace('\n', '') # get rid of '\n' in all fields
        key, val = line.split(':', 1) # take the first 2 tokens from the split statement
        
        if key == 'NEW USER':
            index.append(val)
        
    if line.startswith('amc-general'): 
        temp = re.findall(r'\d+', line)
        # Parsing the values
        key_user_levelfs = float('.'.join(temp[:2]))
        key_inst_levelfs = float('.'.join(temp[2:]))
        #res = [int(i) for i in line.split() if i.isdigit()]
        
        #Adding everything to dict
        d['User_levelfs'].append(key_user_levelfs)
        d['Inst_levelfs'].append(key_inst_levelfs)


df_levelfs = pd.DataFrame(d, index=index)
df_levelfs.to_html(open('df_levelfs.html', 'w'))

print(f"********Parsing and Saving SUs as dataframe********\n")

import matplotlib.pyplot as plt

# Levelfs textfile
Inst_SU = 866880
levelfs=f"SU_{today_formatted}.txt"
with open(levelfs, 'r') as f:
    data = f.readlines()

d = { 'SU(%)': [], }
index = []

for line in data: # go through file line by line
    if line.startswith('NEW USER'): #or line != 'LEVELFS\n': # skip new line characters
        line = line.replace('\n', '') # get rid of '\n' in all fields
        key, val = line.split(':', 1) # take the first 2 tokens from the split statement

        if key == 'NEW USER':
            index.append(val)


    if line.startswith('alpine|amc-general'):
        temp = re.findall(r'\d+', line)
        # Parsing the values
        SU = float(int(temp[-1]) / Inst_SU) * 100
        SU_formatted = '{:.2%}'.format(SU)
        #res = [int(i) for i in line.split() if i.isdigit()]

        #Adding everything to dict
        d['SU(%)'].append(SU)

df_SU = pd.DataFrame(d, index=index)
df_SU.to_html(open('df_SU.html', 'w'))

print(f"********Plotting levelfs********\n")
fig = plt.figure()
df_levelfs.plot.bar(y='User_levelfs', rot=0, figsize=(16, 12),);
plt.xticks(rotation=45)
plt.yticks(fontsize=20)
plt.xticks(fontsize=20)
plt.legend(["levelfs"], fontsize="20", loc ="upper right")
plt.title('User levelfs ' , fontsize=30)
fig.savefig("Top_levelfs.png")


print(f"********Plotting SUs********\n")
fig = plt.figure()
df_SU.plot.bar(y='SU(%)', rot=0, figsize=(16, 12),);
plt.xticks(rotation=45)
plt.yticks(fontsize=20)
plt.xticks(fontsize=20)
plt.legend(["SU(%)"], fontsize="20", loc ="upper right")
plt.title('Top 5 users percentage of SUs' , fontsize=30)
fig.savefig("Top_SUs.png")


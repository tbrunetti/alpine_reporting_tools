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
d = { 'Username': [],
        'User_levelfs': [], 'Inst_levelfs': [], } 

index_levelfs = []
for line in data: # go through file line by line      
    if line.startswith('NEW USER'): #or line != 'LEVELFS\n': # skip new line characters
        line = line.replace('\n', '') # get rid of '\n' in all fields
        key, val = line.split(':', 1) # take the first 2 tokens from the split statement
        
        if key == 'NEW USER':
            index_levelfs.append(val)
        
    if line.startswith('amc-general'): 
        temp = re.findall(r'\d+', line)
        # Parsing the values
        key_user_levelfs = float('.'.join(temp[:2]))
        key_inst_levelfs = float('.'.join(temp[2:]))
        #res = [int(i) for i in line.split() if i.isdigit()]
        
        #Adding everything to dict
        d['User_levelfs'].append(key_user_levelfs)
        d['Inst_levelfs'].append(key_inst_levelfs)
        d['Username'].append(val)

df_levelfs = pd.DataFrame(d,)
df_levelfs.to_html(open('df_levelfs.html', 'w'))

print(f"********Parsing and Saving levelfs as dataframe********\n")

import matplotlib.pyplot as plt

# Levelfs textfile
Inst_SU = 866880
levelfs=f"SU_{today_formatted}.txt"
with open(levelfs, 'r') as f:
    data = f.readlines()

d = { 'Username': [],
        'SU(%)': [], }
index_SU = []

for line in data: # go through file line by line
    if line.startswith('NEW USER'): #or line != 'LEVELFS\n': # skip new line characters
        line = line.replace('\n', '') # get rid of '\n' in all fields
        key, val = line.split(':', 1) # take the first 2 tokens from the split statement

        if key == 'NEW USER':
            index_SU.append(val)


    if line.startswith('alpine|amc-general'):
        temp = re.findall(r'\d+', line)
        # Parsing the values
        SU = float(int(temp[-1]) / Inst_SU) * 100
        SU_formatted = '{:.2%}'.format(SU)
        #res = [int(i) for i in line.split() if i.isdigit()]

        #Adding everything to dict
        d['SU(%)'].append(SU)
        d['Username'].append(val)

df_SU = pd.DataFrame(d,)
df_SU.to_html(open('df_SU.html', 'w'))

user_list_df_SU = []
user_list_df_levelfs = []

for ind,val in enumerate(index_levelfs):
    mask = df_levelfs["Username"] == val
    exec(f'df_levelfs_{ind}= df_levelfs[mask]')
    exec(f'df_SU_{ind}= df_SU[mask]')
    
    # Saving individual dataframes:
    exec(f'df_levelfs_{ind}.to_excel("levelfs_top_{val}_user.xlsx")')
    exec(f'df_SU_{ind}.to_excel("SU_top_{val}_user.xlsx")')
    
    # Storing SUs and levelfs
    exec(f'user_list_df_SU.append(df_SU_{ind})')    
    exec(f'user_list_df_levelfs.append(df_levelfs_{ind})')


print(f"********Plotting levelfs********\n")
df_levelfs.plot.bar(y='User_levelfs', x = 'Username', rot=0, figsize=(12, 8),);
plt.axhline(y=1, color='red', linestyle='dotted', linewidth=2.5)
plt.xlabel('Users', fontsize=18)
plt.ylabel('levelfs', fontsize=16)
plt.xticks(rotation=45)
plt.yticks(fontsize=20)
plt.xticks(fontsize=20)
plt.legend(["levelfs (coeff)"], fontsize="20", loc ="upper right")
plt.title('User levelfs ' , fontsize=30)
plt.savefig("Top_levelfs.png")
plt.show()

print(f"********Plotting SUs********\n")
df_SU.plot.bar(y='SU(%)', x = 'Username', rot=0, figsize=(12, 8),);
plt.axhline(y=20, color='red', linestyle='dotted', linewidth=2.5)
plt.xlabel('Users', fontsize=18)
plt.ylabel('SUs (%)', fontsize=16)
plt.xticks(rotation=45)
plt.yticks(fontsize=20)
plt.xticks(fontsize=20)
plt.legend(["SU(%)"], fontsize="20", loc ="upper right")
plt.title('Top 5 users percentage of SUs' , fontsize=30)
plt.savefig("Top_SUs.png")
plt.show()

print(f"********Plotting individual levelfs and SUs********\n")


for ind, df_ in enumerate(user_list_df_levelfs):
    print(f"********Plotting levelfs********\n")
    df_.plot.bar(y='User_levelfs', x = 'Username', rot=0, figsize=(12, 8),);
    plt.axhline(y=1, color='red', linestyle='dotted', linewidth=2.5)
    #plt.xlabel('Users', fontsize=18)
    plt.ylabel('levelfs coeff', fontsize=16)
    #plt.xticks(rotation=45)
    plt.yticks(fontsize=20)
    plt.xticks(fontsize=20)
    plt.legend(["levelfs"], fontsize="20", loc ="upper right")
    plt.title('User levelfs ' , fontsize=30)
    levelfs=f"Top_user_levelfs_{index_levelfs[ind]}_.png"
    plt.savefig(levelfs)
    plt.show()


for ind, df_ in enumerate(user_list_df_SU):
    print(f"********Plotting SU********\n")
    df_.plot.bar(y='SU(%)', x = 'Username', rot=0, figsize=(12, 8),);
    plt.axhline(y=1, color='red', linestyle='dotted', linewidth=2.5)
    #plt.xlabel('Users', fontsize=18)
    plt.ylabel('SU (%)', fontsize=16)
    #plt.xticks(rotation=45)
    plt.yticks(fontsize=20)
    plt.xticks(fontsize=20)
    plt.legend(["SU (%)"], fontsize="20", loc ="upper right")
    plt.title('User SU ' , fontsize=30)
    SU=f"Top_user_SUs_{index_SU[ind]}_.png"
    plt.savefig(SU)
    plt.show()


print(f"********Done !!!!!!!!!********\n")


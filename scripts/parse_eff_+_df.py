import re
from datetime import datetime
import datetime as DT
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#today_formatted = datetime.today().strftime('%Y-%m-%d')
#today_formatted ='2024-07-08'
# Levelfs textfile
print(f"********Parsing and Saving Efficiency as dataframe********\n")

#eff =f"data_scrape_by_user_dates_START=2024-09-01_END=2024-09-08_reportGeneratedOn_09082024.txt"

eff =f"Eff_Raw_data.txt"

with open(eff, 'r') as f:
    data = f.readlines()
    
    
    
#eff =f"data_scrape_by_user_dates_START=2024-09-01_END=2024-09-08_reportGeneratedOn_09082024.txt"

d = {'Job ID': [], 
     'User': [],
     'State': [],
     'Cores': [],
     'CPU Efficiency': [],
     'Walltime': [],
     'Memory Utilized': [],
     'Memory Efficiency': [],
     } 

user_list = []


for line in data: # go through file line by line   
    if line.startswith('Job ID'):
        line = line.replace('\n', '') # get rid of '\n' in all fields
        key, val = line.split(':', 1) # take the first 2 tokens from the split statement
        val = int(val)
        d['Job ID'].append(val)
        
    elif line.startswith('Cluster'):
        next
    
    elif line.startswith('User/Group'):
        line = line.replace('\n', '') # get rid of '\n' in all fields
        key, val = line.split(':', 1) # take the first 2 tokens from the split statement
        user, group = val.split('/',1)
        d['User'].append(str(user))
        if str(user) not in user_list:
            user_list.append(str(user))
        
    elif line.startswith('State'):
        line = line.replace('\n', '') # get rid of '\n' in all fields
        key, val = line.split(':', 1)
        state, exit = val.split('(',1)
        d['State'].append(str(state))
        
    elif line.startswith('Cores'):
        line = line.replace('\n', '') # get rid of '\n' in all fields
        key, val = line.split(':', 1)
        val = int(val)
        d['Cores'].append(val)
        
    elif line.startswith('CPU Utilized'):
        next
        
    elif line.startswith('CPU Efficiency'):
        line = line.replace('\n', '') # get rid of '\n' in all fields
        key, val = line.split(':', 1)
        eff, text = val.split('%',1)
        val = float(eff)
        d['CPU Efficiency'].append(eff)
        
    elif line.startswith('Job Wall-clock time'):
        line = line.replace('\n', '') # get rid of '\n' in all fields
        key, val = line.split(':', 1)
        d['Walltime'].append(val)  # Convert datetime?
        
    elif line.startswith('Memory Utilized'):
        line = line.replace('\n', '') # get rid of '\n' in all fields
        key, val = line.split(':', 1)
        
        if val.startswith(' 0.00'):
            mem = 0.0
            Bytes = 'MB'
        elif "(estimated maximum)" in val:
            mem = 0.0
            Bytes = 'MB'
        else:
            mem, Bytes = float(val[:-2]), val[-2:]
        

        if Bytes == 'KB':
            convert_mem = 1024.0 * mem
        elif Bytes == 'MB':
            convert_mem = 1024.0 * 1024.0 * mem
        elif Bytes == 'GB':
            convert_mem = 1024.0 * 1024.0 * 1024.0 * mem
        
        d['Memory Utilized'].append(convert_mem )
        
    elif line.startswith('Memory Efficiency'):
        line = line.replace('\n', '') # get rid of '\n' in all fields
        key, val = line.split(':', 1)
        mem_eff, text = val.split('%',1)
        val = float(mem_eff)
        d['Memory Efficiency'].append(mem_eff)

df_eff = pd.DataFrame(d,)

# Saving dataframe
df_eff.to_excel("Eff_all_5_users.xlsx") 


print(f"********Creating and saving individual dataframes for each 5 users********\n")

# Creating individual dataframes for each 5 users:
#
for ind,val in enumerate(user_list):
    mask = df_eff["User"] == val   
    exec(f'df_user_{ind}= df_eff[mask]')
  
    # Saving individual dataframes:
    exec(f'df_user_{ind}.to_excel("Eff_top_{val}_user.xlsx")')


# Reformatting the CPU eff and Mem eff data
df_user_0["CPU Efficiency"]= pd.to_numeric(df_user_0["CPU Efficiency"])
df_user_1["CPU Efficiency"]= pd.to_numeric(df_user_1["CPU Efficiency"])
df_user_2["CPU Efficiency"]= pd.to_numeric(df_user_2["CPU Efficiency"])
df_user_3["CPU Efficiency"]= pd.to_numeric(df_user_3["CPU Efficiency"])
df_user_4["CPU Efficiency"]= pd.to_numeric(df_user_4["CPU Efficiency"])

df_user_0["Memory Efficiency"]= pd.to_numeric(df_user_0["Memory Efficiency"])
df_user_1["Memory Efficiency"]= pd.to_numeric(df_user_1["Memory Efficiency"])
df_user_2["Memory Efficiency"]= pd.to_numeric(df_user_2["Memory Efficiency"])
df_user_3["Memory Efficiency"]= pd.to_numeric(df_user_3["Memory Efficiency"])
df_user_4["Memory Efficiency"]= pd.to_numeric(df_user_4["Memory Efficiency"])

# Plotting and saving the plots for CPU eff
sns.catplot(data=df_user_0, x="State", y="CPU Efficiency",  kind="box")
cpu_efficiency_user = "CPU_eff_user_0.png"
plt.savefig(cpu_efficiency_user)

# Plotting and saving the plots for Mem eff
sns.catplot(data=df_user_0, x="State", y="Memory Efficiency",  kind="box")
mem_efficiency_user = "Mem_eff_user_0.png"
plt.savefig(mem_efficiency_user)


# Plotting and saving the plots for CPU eff
sns.catplot(data=df_user_1, x="State", y="CPU Efficiency",  kind="box")
cpu_efficiency_user = "CPU_eff_user_1.png"
plt.savefig(cpu_efficiency_user)
# Plotting and saving the plots for Mem eff
sns.catplot(data=df_user_1, x="State", y="Memory Efficiency",  kind="box")
mem_efficiency_user = "Mem_eff_user_1.png"
plt.savefig(mem_efficiency_user)

# Plotting and saving the plots for CPU eff
sns.catplot(data=df_user_2, x="State", y="CPU Efficiency",  kind="box")
cpu_efficiency_user = "CPU_eff_user_2.png"
plt.savefig(cpu_efficiency_user)
# Plotting and saving the plots for Mem eff
sns.catplot(data=df_user_2, x="State", y="Memory Efficiency",  kind="box")
mem_efficiency_user = "Mem_eff_user_2.png"
plt.savefig(mem_efficiency_user)


# Plotting and saving the plots for CPU eff
sns.catplot(data=df_user_3, x="State", y="CPU Efficiency",  kind="box")
cpu_efficiency_user = "CPU_eff_user_3.png"
plt.savefig(cpu_efficiency_user)
# Plotting and saving the plots for Mem eff
sns.catplot(data=df_user_3, x="State", y="Memory Efficiency",  kind="box")
mem_efficiency_user = "Mem_eff_user_3.png"
plt.savefig(mem_efficiency_user)

# Plotting and saving the plots for CPU eff
sns.catplot(data=df_user_4, x="State", y="CPU Efficiency",  kind="box")
cpu_efficiency_user = "CPU_eff_user_4.png"
plt.savefig(cpu_efficiency_user)
# Plotting and saving the plots for Mem eff
sns.catplot(data=df_user_4, x="State", y="Memory Efficiency",  kind="box")
mem_efficiency_user = "Mem_eff_user_4.png"
plt.savefig(mem_efficiency_user)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#Reading our data into python
premier_league_data = r'C:\Users\ADMIN\Downloads\Premier_league_champs_data_new.xlsx'
our_df = pd.read_excel(premier_league_data)



our_df['Win percentage per month'] = our_df['Win percentage per month']*100
#Ordering the months as they are in a regular football season
month_order = ['August','September','October','November','December','January','February','March','April','May']

#Getting the average win percentages per month across all seasons combined
monthly_avg = our_df.groupby('Month')['Win percentage per month'].mean()
monthly_avg = monthly_avg.reindex(month_order)

#Creating a contingency table for better ordering
Contingency_table = pd.DataFrame({'month':monthly_avg.index,
                                  'Win percentage':monthly_avg.values})

#plot our findings
sns.set_style('whitegrid')

plt.figure(figsize= (10,6))
sns.heatmap(
    Contingency_table.set_index('month').T,
    annot=True,
    fmt='.2f',
    cmap='coolwarm',
    linewidths=0.5,
    cbar_kws={'label': 'Win percentage'},
    vmin=60,
    vmax=85
)


# Customize the plot
plt.title('Average Win Percentage per Month (Last 10 Years Premier League Champions)', fontsize=16, fontweight='bold')
plt.xlabel('Month', fontsize=14)
plt.ylabel('', fontsize=14)
plt.xticks(rotation=45, fontsize=12)
plt.yticks(fontsize=12)
plt.tight_layout()

plt.show()




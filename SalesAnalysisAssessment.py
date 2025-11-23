# Project statement:

# AAL, established in 2000, is a well-known brand in Australia, particularly recognized for its clothing business.
#  It has opened branches in various states, metropolises, and tier-1 and tier-2 cities across the country.
# The brand caters to all age groups, from kids to the elderly.

# Currently experiencing a surge in business, AAL is actively pursuing expansion opportunities.
#  To facilitate informed investment decisions, the CEO has assigned the responsibility to the head of AAL’s sales and marketing (S&M) department. 
# The specific tasks include:

# Identify the states that are generating the highest revenues.
# Develop sales programs for states with lower revenues. The head of sales and marketing has requested your assistance with this task.
# Analyze the sales data of the company for the fourth quarter in Australia, examining it on a state-by-state basis. 
# Provide insights to assist the company in making data-driven decisions for the upcoming year.



import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd
try:
	import statsmodels.api as sm
except Exception:
	sm = None
	warnings.warn("statsmodels is not installed; continuing without it")

from scipy import stats
from scipy.stats import ttest_1samp
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats.mstats import winsorize
from scipy.stats import boxcox
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

df=pd.read_csv('AusApparalSales4thQrt2020.csv')
print(df)
print(df)
print(df.info())
print(df.describe())
print("============== Identify the states that are generating the highest revenues =======================")
rev_by_state = df.groupby('State')['Sales'].sum().sort_values(ascending=False)
print(rev_by_state)
print("==============  Develop sales programs for states with lower revenues =======================")
low_rev_states = rev_by_state[rev_by_state < rev_by_state.median()]
print(low_rev_states)
print("===============Analyze the sales data of the company for the fourth quarter in Australia, examining it on a state-by-state basis====================")
state_sales_summary = df.groupby('State')['Sales'].agg(['sum', 'mean', 'max', 'min', 'count'])
print(state_sales_summary)
print("===============Provide insights to assist the company in making data-driven decisions for the upcoming year====================")
plt.figure(figsize=(10, 6))
rev_by_state.plot(kind='bar', color='skyblue')
plt.title('Total Sales by State - 4th Quarter 2020')
plt.xlabel('State')
plt.ylabel('Total Sales')
plt.xticks(rotation=45) 
plt.tight_layout()
plt.show()



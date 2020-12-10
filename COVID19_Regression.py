#!/usr/bin/env python
# coding: utf-8

# In[1]:


cd C:\Users\Seema\Desktop\Umber_CS504


# In[2]:


#Importing data analysis packages used in this code
import pandas as pd
import numpy as np


# In[3]:


VDH_Covid=pd.read_csv('VDH COVID19 Cases.txt')


# In[4]:


Full_VA_Data=pd.read_csv('Full_VA_Data.txt',sep='\t', encoding = 'utf-16')


# In[5]:


print(VDH_Covid)


# In[6]:


Full_VA_Data.head()


# In[7]:


#Removing unwanted variables from the orginial data set
full = Full_VA_Data.loc[:,['LHD Name', 'County Name','Ctfips','Stfips', 'CTPopulation', 'HOI_County', 'HOI_CTY_Rank']]
print(full)


# In[8]:


#Sort by HOI_CTY_Rank
VA_df = full.sort_values(by = 'HOI_CTY_Rank')
print(VA_df)


# In[9]:


#Cleaning the data by removing HOIs with 0s and 1s.
full.drop(full.loc[full['HOI_County']==0].index, inplace=True)


# In[10]:


print(full)


# In[11]:


full.drop(full.loc[full['HOI_County']==1].index, inplace=True)
print(full)


# In[12]:


full['HOI_CTY_Rank'] -=1
print(full)


# In[48]:


covid = VDH_Covid.loc[:,['LHD Name','Air Quality','Pop Churning','Pop WeightedDensity','Walkability','Affordability','Education','Food Access', 'Townsend','Income Equality','Job Participation','Employment Access','Health Care Access','Segregation','HOI weighted']]
covid.set_index('LHD Name')


# In[56]:


# calculate the Pearson's correlation between two variables
from numpy.random import randn
from numpy.random import seed
from scipy.stats import pearsonr

# calculate Pearson's correlation
corr, _ = pearsonr(VDH_Covid['Pop Churning'], VDH_Covid['Total Cases'])
print('(Pearsons correlation with Health Care Access): %.3f' % corr)


# In[50]:


from numpy import cov
covariance = cov(covid['Pop Churning'], covid['HOI weighted'])
print(covariance)

#The covariance and covariance matrix are used widely within statistics and 
#multivariate analysis to characterize the relationships between two or more variables.


#The covariance between the two variables. 
#We can see that it is positive, suggesting the variables change in the same direction as we expect.


# In[54]:


from matplotlib import pyplot
pyplot.scatter(covid['Pop Churning'], covid['HOI weighted'])
pyplot.show()


# In[ ]:


corr, _ = pearsonr(covid['Pop Churning'], covid['Number of Cases'])
print('(Pearsons correlation with Health Care Access): %.3f' % corr)


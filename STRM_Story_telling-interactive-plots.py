#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#1.-Introduction" data-toc-modified-id="1.-Introduction-1">1. Introduction</a></span></li><li><span><a href="#2.-First-Steps" data-toc-modified-id="2.-First-Steps-2">2. First Steps</a></span></li><li><span><a href="#3.-Data-Preparation-and-Cleaning" data-toc-modified-id="3.-Data-Preparation-and-Cleaning-3">3. Data Preparation and Cleaning</a></span><ul class="toc-item"><li><span><a href="#3.1.-Drop-Unique-Columns" data-toc-modified-id="3.1.-Drop-Unique-Columns-3.1">3.1. Drop Unique Columns</a></span></li><li><span><a href="#3.2.-Missing-Data" data-toc-modified-id="3.2.-Missing-Data-3.2">3.2. Missing Data</a></span></li><li><span><a href="#3.3.-Outliers" data-toc-modified-id="3.3.-Outliers-3.3">3.3. Outliers</a></span><ul class="toc-item"><li><span><a href="#Fare" data-toc-modified-id="Fare-3.3.1"><code>Fare</code></a></span></li><li><span><a href="#Agevariable" data-toc-modified-id="Agevariable-3.3.2"><code>Age</code>variable</a></span></li></ul></li></ul></li><li><span><a href="#4.-Data-Exploration" data-toc-modified-id="4.-Data-Exploration-4">4. Data Exploration</a></span><ul class="toc-item"><li><span><a href="#4.1.-Embarked-variable" data-toc-modified-id="4.1.-Embarked-variable-4.1">4.1. Embarked variable</a></span><ul class="toc-item"><li><span><a href="#4.1.2.-Embarked-vs-Survived-Stacked-Bar-Chart" data-toc-modified-id="4.1.2.-Embarked-vs-Survived-Stacked-Bar-Chart-4.1.1">4.1.2. <code>Embarked</code> vs <code>Survived</code> Stacked Bar Chart</a></span></li><li><span><a href="#4.1.3.-Age-Box-plots" data-toc-modified-id="4.1.3.-Age-Box-plots-4.1.2">4.1.3. <code>Age</code> Box plots</a></span></li><li><span><a href="#4.1.4.-Sex-Stacked-Bar-Chart" data-toc-modified-id="4.1.4.-Sex-Stacked-Bar-Chart-4.1.3">4.1.4. <code>Sex</code> Stacked Bar Chart</a></span></li><li><span><a href="#4.1.5.-Fare-Box-Plot" data-toc-modified-id="4.1.5.-Fare-Box-Plot-4.1.4">4.1.5. <code>Fare</code> Box Plot</a></span></li><li><span><a href="#4.1.6.-PClass-Grouped-Bar-Plot" data-toc-modified-id="4.1.6.-PClass-Grouped-Bar-Plot-4.1.5">4.1.6. <code>PClass</code> Grouped Bar Plot</a></span></li></ul></li></ul></li></ul></div>

# # 1. Introduction
# <a class="anchor" id="1"></a>
# 
# [^ Index](#index)

#     The objectives are: 
#         1 - Prepare your data for the visualization tasks: data cleaning
#         2 - Explore your data and create cool plots
#         
# **Variable information:**        
# ![image.png](attachment:image.png)

# # 2. First Steps
# <a class="anchor" id="2"></a>
# 
# [^ Index](#index)

# In[1]:


#Import common modules
import pandas as pd
pd.options.mode.chained_assignment = None

import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import matplotlib
import plotly.express as px
import plotly.graph_objs as go

import warnings
warnings.filterwarnings('ignore')


# In[2]:


# Execute this line (of course, modifying the path)
import sys
sys.path.insert(0, 'G:/Mi unidad/DS_CURRICULUM_FT/_functions_')

from Functions_EDA import *


# In[53]:


data = pd.read_csv('clean_titanic.csv', index_col=0)


# # 4. Data Exploration
# <a class="anchor" id="4"></a>
# 
# [^ Index](#index)

#     We'll Explore the data by visualizing and then noting patterns and relationships between different   
#     variables to try and get an out of the box view as mush as possible, later this can help us impute the    'Age' 
#     which is first in order alphabetically but we'll leave it last to get a better understanding and impute it 
#     better than just replacing missing values with the median.

# ## 4.1. Embarked variable
# <a class="anchor" id="4.1"></a>
# 
# 
# [^ Index](#index)

#         Passengers on the Titanic embarked from three locations: Cherbourg, Queenstown and Southampton.
#         Let's explore where the passengers embarked from and is there any obvious influence for survival.

# In[54]:


def get_percentages(df,name_column):
    percentage = df[name_column].value_counts(normalize=True)*100
    percentage = percentage.reset_index()
    percentage.columns = [name_column,'percentage']
    percentage = percentage.sort_values(by=name_column)
    return percentage


# In[55]:


count_Embarked = get_percentages(df, 'Embarked')
count_Embarked


# In[58]:


color_list = ['DarkCyan', 'GreenYellow', 'Orchid']


#     Bar chart

# In[64]:


fig = px.bar(count_Embarked, x = 'Embarked', y = 'percentage',text= 'percentage',
            color= 'Embarked', color_discrete_sequence = color_list).update_traces(texttemplate='%{text:.2s} %')
fig.show()


# ### 4.1.2. `Embarked` vs `Survived` Stacked Bar Chart
# <a class="anchor" id="4.1.2."></a>

# In[62]:


survived_Embarked = get_percentages(df[df['Survived'] == 1] , 'Embarked')
survived_Embarked


# In[65]:


fig = px.bar(survived_Embarked, x = 'Embarked', y = 'percentage',text= 'percentage',
            color= 'Embarked', color_discrete_sequence = color_list).update_traces(texttemplate='%{text:.2s} %')

fig.show()


# In[66]:


survived_Embarked = get_percentages(df[df['Survived'] == 0] , 'Embarked')
survived_Embarked


# In[67]:


fig = px.bar(survived_Embarked, x = 'Embarked', y = 'percentage',text= 'percentage',
            color= 'Embarked', color_discrete_sequence = color_list).update_traces(texttemplate='%{text:.2s} %')

fig.show()


# ### 4.1.3. `Age` Box plots
# <a class="anchor" id="4.1.3."></a>
# 
#     Which of the ports embarked the youngest population range?

# In[ ]:


df.Age.describe().T


# In[ ]:


df['Age'] = df['Age'].astype('int')
df[df.Embarked == 'Queenstown']['Age'].value_counts()


# In[ ]:


df.groupby('Embarked').describe().T


# In[ ]:


fig = px.box(df,x= 'Embarked', y= 'Age',color= 'Embarked',
             color_discrete_sequence=['Coral', 'Gold', 'Lightgreen'],
            title = 'Age amongst Embark Points')
fig.show()


# ### 4.1.4. `Sex` Stacked Bar Chart
# <a class="anchor" id="4.1.4."></a>
# 
#     and what about the Gender?

# In[76]:


embarked_count_male = get_percentages(df[df['Sex'] == 'male'] , 'Embarked')
embarked_count_male['Sex'] = 'male'
embarked_count_male


# In[73]:


embarked_count_female = get_percentages(df[df['Sex'] == 'female'] , 'Embarked')
embarked_count_female['Sex'] = 'female'


# In[77]:


embarked_sex = pd.concat([embarked_count_male,
                          embarked_count_female], axis=0)
embarked_sex 


# In[81]:


fig = px.bar(embarked_sex, x= 'Embarked', y="percentage", color='Sex',
            color_discrete_sequence=color_list)

#fig.update_layout(title_text='Least Used Feature')
fig.show()


# ### 4.1.5. `Fare` Box Plot
# <a class="anchor" id="4.1.5."></a>

# In[ ]:


fig = px.box(df,x= 'Embarked', y= 'Fare',color= 'Embarked',
             color_discrete_sequence=['Coral', 'Gold', 'Lightgreen'],
            title = 'Embarkment and Fares')
fig.show()


# ### 4.1.6. `PClass` Grouped Bar Plot
# <a class="anchor" id="4.1.6."></a>
# [Index](#index)

# In[ ]:


df['Pclass'].value_counts()


# In[ ]:


#Passenger Class
embarked_count_Pclass1 = df[df['Pclass'] == 1].groupby(['Embarked'], as_index= True).count()['Pclass']

embarked_count_Pclass2 = df[df['Pclass'] == 2].groupby(['Embarked'], as_index=True, 
                                                       sort=True).count()['Pclass']
embarked_count_Pclass3 = df[df['Pclass'] == 3].groupby(['Embarked'], as_index=True,
                                                       sort=True).count()['Pclass']


# In[ ]:


embarked_count_Pclass3


# In[ ]:


df[df.Survived==0].groupby(['Embarked', 'Sex', 'Pclass']).count()['Survived']


# In[ ]:


embarked_count_Pclass1 = embarked_count_Pclass1.reset_index()
embarked_count_Pclass1.columns = ['Embarked', 'Pclass1']
embarked_count_Pclass1


# In[ ]:


embarked_count_Pclass2 = embarked_count_Pclass2.reset_index()
embarked_count_Pclass2.columns = ['Embarked', 'Pclass2']
embarked_count_Pclass2


# In[ ]:


embarked_count_Pclass3 = embarked_count_Pclass3.reset_index()
embarked_count_Pclass3.columns = ['Embarked', 'Pclass3']
embarked_count_Pclass3


# **Python Figure Reference**
# 
# `barnorm`
# - Parent: layout
# - Type: enumerated , one of ( "" | "fraction" | "percent" )
# - Default: ""
# 
#         Sets the normalization for bar traces on the graph. With "fraction", the value of each bar is divided by the sum  of all values at that location coordinate. "percent" is the same but multiplied by 100 to show percentages.

# In[ ]:


## BarPlot 1: just adding the value that you have in your variable y. Layout->> default: 
#barnome = ''
# a) embarked_count_Pclass3: 
                            #Cherbourg       66
                            #Queenstown      72
                            #Southampton    353

embarked_bar_Pclass1 = go.Bar(x=embarked_count_Pclass1['Embarked'], 
                              y=embarked_count_Pclass1['Pclass1'], 
                              name='Upper Class')

embarked_bar_Pclass2 = go.Bar(x=embarked_count_Pclass2['Embarked'], 
                              y=embarked_count_Pclass2['Pclass2'],
                              name='Middle Class')

embarked_bar_Pclass3 = go.Bar(x=embarked_count_Pclass3['Embarked'], 
                              y=embarked_count_Pclass3['Pclass3'],
                              name='Lower Class')

embarked_Pclass_layout = go.Layout(title='Embarkment and Passenger Class')
embarked_Pclass_fig = go.Figure(data = [embarked_bar_Pclass1, embarked_bar_Pclass2, 
                                        embarked_bar_Pclass3], layout=embarked_Pclass_layout)


embarked_Pclass_fig.show()


# In[ ]:


## BarPlot2: Layout->> barnome = 'fraction'
                       #the value of each bar is divided by the sum  of all values at that location coordinate
#  a) embarked_count_Pclass1:                           a) embarked_count_Pclass2: 
            #Cherbourg       85                                Cherbourg       17
                            
# c) embarked_count_Pclass3:    
          #Cherbourg       66 --> ToTAL = 85+66+17 = 168   

# Outcome: a) Pclass1 85/168 = 0.51  ; b) Pclass2  17/168 =0.10  ; c) Pclass3 : 66/168 = 0.39
    

embarked_bar_Pclass1 = go.Bar(x=embarked_count_Pclass1['Embarked'], y=embarked_count_Pclass1['Pclass1'], 
                              name='Upper Class')

embarked_bar_Pclass2 = go.Bar(x=embarked_count_Pclass2['Embarked'], y=embarked_count_Pclass2['Pclass2'],
                              name='Middle Class')

embarked_bar_Pclass3 = go.Bar(x=embarked_count_Pclass3['Embarked'], y=embarked_count_Pclass3['Pclass3'],
                              name='Lower Class')

embarked_Pclass_layout = go.Layout(title='Embarkment and Passenger Class',
                                   barnorm = 'fraction')

embarked_Pclass_fig = go.Figure(data = [embarked_bar_Pclass1, embarked_bar_Pclass2, 
                                        embarked_bar_Pclass3], layout=embarked_Pclass_layout)


embarked_Pclass_fig.show()


# In[ ]:


## BarPlot3: Layout->> barnome = 'percent'
                       #the value of each bar is divided by the sum  of all values at that location coordinate
#  a) embarked_count_Pclass1:                           a) embarked_count_Pclass2: 
            #Cherbourg       85                                Cherbourg       17
                            
# c) embarked_count_Pclass3:    
          #Cherbourg       66 --> ToTAL = 85+66+17 = 168   

# Outcome: a) Pclass1 85/168 *100 = 51  ; b) Pclass2  17/168*100 =10  ; c) Pclass3 : 66/168*100 = 39
    

embarked_bar_Pclass1 = go.Bar(x=embarked_count_Pclass1['Embarked'], y=embarked_count_Pclass1['Pclass1'], 
                              name='Upper Class')

embarked_bar_Pclass2 = go.Bar(x=embarked_count_Pclass2['Embarked'], y=embarked_count_Pclass2['Pclass2'],
                              name='Middle Class')

embarked_bar_Pclass3 = go.Bar(x=embarked_count_Pclass3['Embarked'], y=embarked_count_Pclass3['Pclass3'],
                              name='Lower Class')

embarked_Pclass_layout = go.Layout(title='Embarkment and Passenger Class',barnorm = 'percent')

embarked_Pclass_fig = go.Figure(data = [embarked_bar_Pclass1, embarked_bar_Pclass2, 
                                        embarked_bar_Pclass3], layout=embarked_Pclass_layout)


embarked_Pclass_fig.show()


#     1.Most passengers embarked from Southampton, then Cherbourg followed by Queenstown .
#  
#     2.Passengers who embarked from Southampton and Queenstown had less survivals, although the survival rate is 
#     relatively low for Southampton passengers, but what is unique is that Cherbourg passengers had more 
#     survivors!
#  
#     3.The median of ages for all embark points are somehow similar, although Southampton passengers have more 
#     elderly.
#     
#     4.Sex distribution amongst embark points looks reasonable where number of males are always higher..
#     
#     5.Fare distribution and passengers' classes tells a story for each embarkment point : 
#         Cherbourg: A median as high as 29.7$ can be misleading, this embarkment point had 66 lower class and
#     85 upper class with 17 of middle class, this tells us that it's almost a 50-50 split between the 
#     rich and the poor, not overlooking a rocketing value of 512$ and multiple fares in the range of 
#         200$.
#         
#         Queenstown: A low median of 7.5$ for fares, the distribution of passenger classes reinforce the fact
#         that most of the passengers from this point were less fortunate. Although there's two upper class
#         and 3 middle class passengers.
#         
#         Southampton: The point that most passengers embarked from, with very high variance, but we can tell
#         that the majority of the passengers were at the lower class.
#         
# 

# In[ ]:


# Exercise 1. Can you think in another visualizations that might be useful considering those variables?


# In[ ]:





# In[ ]:


# Exercise 2. Are any of the other variables interesting for you? (Answer: compulsary YES :)) Perform the same analysis 
# with at least two more variables and extract some conclusions


# In[ ]:





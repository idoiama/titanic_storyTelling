
#Import common modules
import streamlit as st
import pandas as pd
pd.options.mode.chained_assignment = None

import numpy as np
import plotly.express as px

import warnings
warnings.filterwarnings('ignore')


# PAGE STYLING
st.set_page_config(page_title="Titanic Dashboard ", 
                   page_icon=":ship:",
                   layout='wide')
                   
st.title("Welcome to the ***Titanic*** dashboard! : :star:")
"""
[Titanic] (https://en.wikipedia.org/wiki/Titanic)
RMS Titanic was a British passenger liner, operated by the White Star Line, which sank in the North Atlantic Ocean on 15 April 1912 after striking an iceberg during her maiden voyage from Southampton, UK, to New York City. Of the estimated 2,224 passengers and crew aboard, more than 1,500 died, which made the sinking possibly one of the deadliest for a single ship up to that time. [a] It remains to this day the deadliest peacetime sinking of a superliner or cruise ship.[4] 
The disaster drew much public attention, provided foundational material for the disaster film genre and has inspired many artistic work
"""
# Page styling
title_image = Image.open("titanic.jpg")
st.image(title_image)
st.markdown("Let's ask the following question: ***'Can we use Python to retrive information from the titanic?' ***")

st.header("**Overall information from Titanic**")
"""
Bla bla bla information from Titanic bla bla bla"""



df = pd.read_csv('clean_titanic.csv', index_col=0)


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


# In[65]:


fig = px.bar(survived_Embarked, x = 'Embarked', y = 'percentage',text= 'percentage',
            color= 'Embarked', color_discrete_sequence = color_list).update_traces(texttemplate='%{text:.2s} %')

fig.show()


# In[66]:


survived_Embarked = get_percentages(df[df['Survived'] == 0] , 'Embarked')


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




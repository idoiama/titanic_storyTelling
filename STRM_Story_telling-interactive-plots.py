
#Import common modules
import streamlit as st
import pandas as pd
pd.options.mode.chained_assignment = None
from PIL import Image

import numpy as np
import plotly.express as px

import warnings
warnings.filterwarnings('ignore')
def get_percentages(df,name_column):
    percentage = df[name_column].value_counts(normalize=True)*100
    percentage = percentage.reset_index()
    percentage.columns = [name_column,'percentage']
    percentage = percentage.sort_values(by=name_column)
    return percentage


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


#Data loading and first checks
df = pd.read_csv('clean_titanic.csv', index_col=0)
color_list = ['DarkCyan', 'GreenYellow', 'Orchid']


# 4. Data Exploration
#     We'll Explore the data by visualizing and then noting patterns and relationships between different   
#     variables to try and get an out of the box view as mush as possible, later this can help us impute the    'Age' 
#     which is first in order alphabetically but we'll leave it last to get a better understanding and impute it 
#     better than just replacing missing values with the median.


col1, col2 = st.beta_columns(2)

with col1:

    st.subheader('Distribution of Ages vs Sex vs Survival rate')
    fig = px.scatter(df,x= 'Age', y = 'Survived',color= 'Sex',
                 color_discrete_sequence = color_list)
    st.plotly_chart(fig)

with col2:
    st.subheader('Distribution of Gender')
    fig = px.histogram(df,x= 'Sex',color= 'Sex',
                 color_discrete_sequence = color_list)
    st.plotly_chart(fig)

    
 ################ FILTER BY PORTS: multiple ports at the same time ###########  
all_ports = df.Embarked.unique().tolist()
st.subheader('**Select the all_port/s you want to explore**')
langs = st.multiselect(' ',options=all_ports, default=all_ports)

## 4.1. Embarked variable

plot_df = df[df.Embarked.isin(langs)]
count_Embarked = get_percentages(plot_df, 'Embarked')

st.subheader('Distribution of people who embarked in the selected ports')
fig = px.bar(count_Embarked, x = 'Embarked', y = 'percentage',text= 'percentage',
            color= 'Embarked', color_discrete_sequence = color_list).update_traces(texttemplate='%{text:.2s} %')
st.plotly_chart(fig)

## Showing the Survival information into two different columns

plot_1 = plot_df[plot_df['Survived'] == 1]
count_1 = get_percentages(plot_1, 'Embarked')

plot_0 = plot_df[plot_df['Survived'] == 0]
count_0 = get_percentages(plot_0, 'Embarked')

col1, col2 = st.beta_columns(2)
with col1:
    st.subheader('Rate of people who survived')
    fig1 = px.bar(count_1, x = 'Embarked', y = 'percentage',text= 'percentage',
            color= 'Embarked',color_discrete_sequence = color_list).update_traces(texttemplate='%{text:.2s} %')
    st.plotly_chart(fig1)  
    
with col2:
    st.subheader('Rate of people who did not survived')
    fig2 =  px.bar(count_0, x = 'Embarked', y = 'percentage',text= 'percentage',
            color= 'Embarked', color_discrete_sequence = color_list).update_traces(texttemplate='%{text:.2s} %')            
    st.plotly_chart(fig2)
    
############################################################################################
# ZOOM INTO ONE PORT
############################################################################################

st.title('Dive into the Embarked Ports!')
all_ports = df.Embarked.unique().tolist()
options = st.selectbox(
 'Which port are you interested in diving in?', all_ports)

#Filter the information for this port specifically
ind_port = df[df.Embarked == options]

st.subheader('Distribution of people in the different classes')
classes_ = get_percentages(ind_port, 'Pclass')

fig3 = px.pie(classes_, values='percentage', color= 'Pclass',names= 'Pclass', title = 'Class distribution',
               color_discrete_sequence = color_list).update_traces(textposition='inside', textinfo='percent')
st.plotly_chart(fig3)


st.subheader('People that did not survived')
sex_ = get_percentages(ind_port , 'Sex')
fig4 = px.pie(sex_, values='percentage', color= 'Sex',names= 'Sex', title = 'Sex distribution',
               color_discrete_sequence = color_list).update_traces(textposition='inside', textinfo='percent')
st.plotly_chart(fig4)

##############################################################################################
# Customize the dashboard with some input data
##############################################################################################
# a) One specific number as input 

age_in = st.number_input('Let's zoom in into a range of ages: enter your age')
#text_input() for text
ages = df[df['Age'] > int(age_in)]

col1, col2 = st.beta_columns(2)
with col1:
    st.subheader('Distribution of ages, according to your input')
    fig = px.box(ages,x= 'Embarked', y= 'Age',color= 'Embarked',
             color_discrete_sequence=color_list,
            title = 'Age amongst Embark Points')
    st.plotly_chart(fig)

with col2:
    st.subheader('Distribution of sex, according to your input')
    fig = px.histogram(ages,x= 'Sex',color= 'Embarked',
             color_discrete_sequence=color_list,
            title = 'Sex amongst Embark Points')
    st.plotly_chart(fig)
    
# b) Bar slider    
age_in = st.slider("Let's zoom in into a range of ages: enter your age", min_value=0, max_value=80)
#text_input() for text
#age_in = int(age_in)
print(type(age_in))
ages = df[df['Age'].isin(age_in)]

col1, col2 = st.beta_columns(2)
with col1:
    st.subheader('Distribution of ages, according to your input')
    fig = px.box(ages,x= 'Embarked', y= 'Age',color= 'Embarked',
             color_discrete_sequence=color_list,
            title = 'Age amongst Embark Points')
    st.plotly_chart(fig)

with col2:
    st.subheader('Distribution of sex, according to your input')
    fig = px.histogram(ages,x= 'Sex',color= 'Embarked',
             color_discrete_sequence=color_list,
            title = 'Sex amongst Embark Points')
    st.plotly_chart(fig)  
    
    
# ### 4.1.4. `Sex` Stacked Bar Chart
# <a class="anchor" id="4.1.4."></a>
# 
#     and what about the Gender?

# In[76]:


embarked_count_male = get_percentages(df[df['Sex'] == 'male'] , 'Embarked')
embarked_count_male['Sex'] = 'male'


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




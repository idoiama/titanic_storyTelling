
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

    st.subheader('Distribution of classes')
    fig = px.pie(df, value= 'Pclass',
                color = 'Pclass',color_discrete_sequence = color_list)
    fig.update_traces(texttemplate='%{text:.2s} %', textposition='inside')
    st.plotly_chart(fig)

with col2:
    st.subheader('Distribution of Gender in all Embarked ports')
    fig = px.bar(df, x='Embarked', y = 'Sex',
                color = 'Sex',color_discrete_sequence = color_list)
    fig.update_traces(texttemplate='%{text:.2s} %', textposition='inside')
    st.plotly_chart(fig)

all_ports = df.Embarked.unique().tolist()
st.subheader('**Select the all_port/s you want to explore**')
langs = st.multiselect(' ',options=all_ports, default=all_ports)


# ## 4.1. Embarked variable

################ FILTER BY PORTS ###########
plot_df = df[df.Embarked.isin(langs)]
count_Embarked = get_percentages(plot_df, 'Embarked')


fig = px.bar(count_Embarked, x = 'Embarked', y = 'percentage',text= 'percentage',
            color= 'Embarked', color_discrete_sequence = color_list).update_traces(texttemplate='%{text:.2s} %')
st.plotly_chart(fig)

## Showing the info into two different columns
col1, col2 = st.beta_columns(2)
with col1:
    st.subheader('Subplot1')
    fig1 = px.bar(count_Embarked, x = 'Embarked', y = 'percentage',text= 'percentage',
            color= 'Embarked',color_discrete_sequence = color_list).update_traces(texttemplate='%{text:.2s} %')
    st.plotly_chart(fig1)  
    
with col2:
    st.subheader('Subplot2')
    fig2 =  px.bar(count_Embarked, x = 'Embarked', y = 'percentage',text= 'percentage',
            color= 'Embarked').update_traces(texttemplate='%{text:.2s} %')            
    st.plotly_chart(fig2)
    
    
st.title('Dive into the Embarked Ports!')
all_ports = df.Embarked.unique().tolist()
options = st.selectbox(
 'Which port are you interested in diving in?', all_ports)
#Filter the information for this port specifically

ind_port = df[df.Embarked == options]

st.subheader('People that survived')
survived_Embarked = get_percentages(ind_port[ind_port['Survived'] == 1] , 'Embarked')
fig3 = px.bar(survived_Embarked, x = 'Embarked', y = 'percentage',text= 'percentage',
            color= 'Embarked', color_discrete_sequence = color_list).update_traces(texttemplate='%{text:.2s} %')

st.plotly_chart(fig3)


st.subheader('People that did not survived')
survived_Embarked = get_percentages(ind_port[ind_port['Survived'] == 0] , 'Embarked')
fig4 = px.bar(survived_Embarked, x = 'Embarked', y = 'percentage',text= 'percentage',
            color= 'Embarked', color_discrete_sequence = color_list).update_traces(texttemplate='%{text:.2s} %')
st.plotly_chart(fig4)


name = st.sidebar.text_input('''Let's zoom in into a range of ages: enter your age''')
ages = df[df['Age'] > name]

# ### 4.1.3. `Age` Box plots
# <a class="anchor" id="4.1.3."></a>
fig = px.box(ages,x= 'Embarked', y= 'Age',color= 'Embarked',
             color_discrete_sequence=['Coral', 'Gold', 'Lightgreen'],
            title = 'Age amongst Embark Points')
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




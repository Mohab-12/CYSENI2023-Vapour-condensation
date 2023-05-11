#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# import matplotlib.animation as animation
# from matplotlib.animation import FuncAnimation, writers


# In[2]:


#sns.set_theme(style='whitegrid', palette='pastel')
plt.style.use('ggplot')


# In[3]:


df=pd.read_excel(r"Horizontalus ruozas-Eksperimetu suvestine.xlsb.xlsx", sheet_name='Sheet3')


# In[4]:


df.drop(columns='Heat lost ', inplace=True)
#df.dropna(inplace=True)


# In[5]:


df['Mixture tin, oC']=df['Mixture tin, oC'].astype('float')


# In[6]:


# df.columns


# In[7]:


a=df.loc[df['Re']==5000][['First_Cond', 'Second_Cond', 'Third_Cond', 'Fourth_Cond',
       'Fifth_Cond', 'Sixth_Cond', 'Seventh_Cond', 'Eighth_Cond','Mixture tin, oC']]
c=df.loc[df['Re']==5000][[ 'First_heat_Coef', 'Second_heat_Coef', 'Third_heat_Coef',
       'Fourth_heat_Coef', 'Fifth_heat_Coef', 'Sixth_heat_Coef',
       'Seventh_heat_Coef', 'Eighth_heat_Coef','Mixture tin, oC']]
e=df.loc[df['Re']==5000][['First_Nusselt', 'Second_Nusselt', 'Third_Nusselt', 'Fourth_Nusselt',
       'Fifth_Nusselt', 'Sixth_Nusselt', 'Seventh_Nusselt', 'Eighth_Nusselt','Mixture tin, oC']]


# In[8]:


Nusselt = e.T
Heat_transfer_coefficient = c.T
Rate_of_Condensation = a.T


# In[9]:


import streamlit as st

st.write("""
            # Plotting parameters against temperature at `Re = 5000` and `mass fraction  = 20%`
            """)


# In[10]:


Nusselt.iloc[-1:].values.ravel()


# In[11]:


import plotly.express as px
import streamlit as st

T1 = st.sidebar.selectbox(label='Choose a parameter to plot', options=['Nusselt number',
                                                                       'Heat transfer coefficient',
                                                                       'Rate of Condensation'])
if T1=='Nusselt number':
    T1=Nusselt
    st.write(T1)
    col='Nusselt'
    T2 = st.sidebar.selectbox(label='Choose your Temperature', options=T1.iloc[-1:].values.ravel())
    column_name = T1.columns[T1.eq(T2).any()][0]
    fig = px.line(x = T1.index[:-1], y=T1.iloc[:-1, column_name])
    fig.update_layout(
            xaxis_title=col,
            yaxis_title="Nusselt number")
    st.write(fig)
elif T1=='Heat transfer coefficient':
    T1=Heat_transfer_coefficient
    st.write(T1)
    col='Heat transfer coefficient'
    T2 = st.sidebar.selectbox(label='Choose your Temperature', options=T1.iloc[-1:].values.ravel())

    column_name = T1.columns[T1.eq(T2).any()][0]
    fig = px.line(x = T1.index[:-1], y=T1.iloc[:-1, column_name])
    fig.update_layout(
            xaxis_title=col,
            yaxis_title="Heat transfer coefficient ((W/m²K))")
    st.write(fig)
else: 
    T1=Rate_of_Condensation
    col='Rate of condensation'
    st.write(T1)
    T2 = st.sidebar.selectbox(label='Choose your Temperature', options=T1.iloc[-1:].values.ravel())
    column_name = T1.columns[T1.eq(T2).any()][0]
    fig = px.bar(x = T1.index[:-1], y=T1.iloc[:-1, column_name])
    fig.update_layout(
        xaxis_title=col,
        yaxis_title="Rate of Condensation (kg/min)")
    st.write(fig)


# In[ ]:





# In[ ]:





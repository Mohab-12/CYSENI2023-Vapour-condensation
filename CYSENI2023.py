#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
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
            # Plotting parameters against temperature at  
            ## `Re = 5000` and `mass fraction = 20%`
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
    col='Nusselt'
    T2 = st.sidebar.selectbox(label='Choose your Temperature', options=T1.iloc[-1:].values.ravel())
    column_name = T1.columns[T1.eq(T2).any()][0]
    fig = px.line(x = T1.index[:-1], y=T1.iloc[:-1, column_name], markers=True)
    fig.update_layout(
            xaxis_title=col,
            yaxis_title="Nusselt number")
    fig.update_xaxes(
    tickvals=[0,1, 2, 3, 4, 5, 6, 7,],
    ticktext=[1, 2, 3, 4, 5, 6, 7, 8])
    st.write(fig)
elif T1=='Heat transfer coefficient':
    T1=Heat_transfer_coefficient
    col='Heat transfer coefficient'
    T2 = st.sidebar.selectbox(label='Choose your Temperature', options=T1.iloc[-1:].values.ravel())

    column_name = T1.columns[T1.eq(T2).any()][0]
    fig = px.line(x = T1.index[:-1], y=T1.iloc[:-1, column_name], markers=True)
    fig.update_layout(
            xaxis_title=col,
            yaxis_title="Heat transfer coefficient ((W/m²K))")
    fig.update_xaxes(
    tickvals=[0,1, 2, 3, 4, 5, 6, 7],
    ticktext=[1, 2, 3, 4, 5, 6, 7, 8])
    st.write(fig)
else: 
    T1=Rate_of_Condensation
    col='Rate of condensation'
    T2 = st.sidebar.selectbox(label='Choose your Temperature', options=T1.iloc[-1:].values.ravel())
    column_name = T1.columns[T1.eq(T2).any()][0]
    # Assuming your DataFrame is called df
    # Select the first eight rows
    df_selected = Rate_of_Condensation.iloc[:8]

    # Reset the index
    df_selected.reset_index(drop=True, inplace=True)

    # Create a new column to group the rows in pairs
    df_selected['group'] = (df_selected.index // 2) + 1

    # Group by the 'group' column and sum the values of each group
    df_summed = df_selected.groupby('group').sum()

    # Reset the index to get the final result with four rows
    df_summed.reset_index(drop=True, inplace=True)

    # Create a new column to group the rows in pairs
    df_selected['group'] = (df_selected.index // 2) + 1

    # Group by the 'group' column and sum the values of each group
    df_summed = df_selected.groupby('group').sum()

    # Reset the index to get the final result with four rows
    df_summed.reset_index(drop=True, inplace=True)
 
    fig = px.bar(x = [1,2,3,4], y=(df_summed.iloc[:, column_name]*3)/1000)
    fig.update_layout(
        xaxis_title=col,
        yaxis_title="Rate of Condensation (Kg/min)")
    fig.update_xaxes(
    tickvals=[1, 2, 3, 4],
    ticktext=[1, 2, 3, 4])
    st.write(fig)


# In[ ]:
check1 = st.checkbox('Click here for temperature profile')

if check1==True:
    Temperature_of_mixture = [113.8721369,
                              107.6319682,
                              103.665735, 
                              98.40364976,
                              96.73604539,
                              91.28107915,
                              88.70575529,
                              83.74964505]

    Temperature_of_cooling_water = [29.6592803,
                                    28.01903525,
                                    26.14824476,
                                    24.0725242,
                                    21.81748892,
                                    19.4087543,
                                    16.87193569,
                                    14.23264846]

    fig = px.line(x=[1, 2, 3, 4, 5, 6, 7, 8], y=[Temperature_of_mixture, Temperature_of_cooling_water],
                  color_discrete_sequence=['blue', 'green'], markers=True)
    fig.update_layout(
            xaxis_title='Local points',
            yaxis_title="Temperatures (C)",
            showlegend=True)
    fig.update_xaxes(
    tickvals=[1, 2, 3, 4, 5, 6, 7, 8],
    ticktext=[1, 2, 3, 4, 5, 6, 7, 8])

    fig.data[0].name = 'Mixture Temperature'
    fig.data[1].name = 'Cooling Water Temperature'
    
    triangle_vertices1 = [(4.8, np.median(Temperature_of_mixture)),
                         (4.6,np.median(Temperature_of_mixture)+2),
                         (4.6,np.median(Temperature_of_mixture)-2)]

    triangle_vertices2 = [(4.5, np.median(Temperature_of_cooling_water)),
                         (4.8,np.median(Temperature_of_cooling_water)+1),
                         (4.8,np.median(Temperature_of_cooling_water)-2)]

    shape1 = go.layout.Shape(
        type='path',
        path=f'M {triangle_vertices1[0][0]} {triangle_vertices1[0][1]} L {triangle_vertices1[1][0]} {triangle_vertices1[1][1]} '
             f'L {triangle_vertices1[2][0]} {triangle_vertices1[2][1]} Z',
        fillcolor='blue',
        opacity=0.5,
        line=dict(width=0)
    )

    # Create a shape for the second triangle
    shape2 = go.layout.Shape(
        type='path',
        path=f'M {triangle_vertices2[0][0]} {triangle_vertices2[0][1]} L {triangle_vertices2[1][0]} {triangle_vertices2[1][1]} '
             f'L {triangle_vertices2[2][0]} {triangle_vertices2[2][1]} Z',
        fillcolor='green',
        opacity=0.5,
        line=dict(width=0)
    )

    # Add the shapes to the layout
    fig.update_layout(shapes=[shape1, shape2])

    st.write(fig)
    
    
    
check2 = st.checkbox('Click here for Condensation efficiecny')

if check2==True:
    df['Condensation efficiecny'].fillna(0, inplace=True)
    fig = px.scatter(df, x='Mixture tin, oC', y='Condensation efficiecny', color='Condensation efficiecny',
                 size='Condensation efficiecny')
    st.write(fig)

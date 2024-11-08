import streamlit as st 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

def dashboard_page():
    st.title('Dashboard View')


    #load data
    data = pd.read_excel('trainset.xlsx')

    st.header('Data Overview')
    st.write('Here is a quick sumarry of the dataset')
    st.dataframe(data.head())

    st.subheader('Churn Count')

    # churn_count = data['Churn'].value_counts()
    # st.bar_chart(churn_count)

    # plot correlation plot 
    st.subheader('correlation')
    corr = data[['tenure','TotalCharges']].corr()

    plt.figure(figsize=(10, 6))
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    st.pyplot(plt)
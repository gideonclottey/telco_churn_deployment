import streamlit as st
from PIL import Image

image = Image.open(r'Telcom.png')
st.image(image, width=100)

def home_page():
    st.title('Telco Churn Classification Project')
    st.divider()
    st.markdown('''This uses machine learning to classify whether a customer is likely to church or not''')
    st.subheader('Instructions')
    st.markdown('''
- Upload a csv file
- Select the features from classification 
- Choose a machine learning model from the dropdown
- Click on the 'Classify' to get the predicted results.
- The app gives you a report on the performance of the model
- Expect it to give metrics like f1 score , recall, precision and accuracy
                ''')
    st.subheader('App Features')
    st.markdown(''' 
- **Data View** : Access the customer data
- **Dashboard** : Shows Data visualization for insights

    ''')

    st.subheader('User Benefits')
    st.markdown(''' 
- **Data Driven Decision** : You make informed decision backed by data
- **Access Machine Learning** : Utulise machine Learning algorithm 

''')
    st.write('### How to Run the application')
    st.code(''' 
#Activate the Virtual Environment
env/scripts/activate
#Run the App
streamlit run p.py

''')
    

   
    st.write('--'*30)
    st.write('Contact Me')


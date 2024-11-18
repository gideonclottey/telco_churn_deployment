import streamlit as st 
import pickle
import pandas as pd

#load the pipeline

@st.cache_resource
def load_pipline():
    with(open('models/pipeline.pkl', 'rb') as file):
        return pickle.load(file)
        
def load_model(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)
        

def predict_page():
    st.title('Prediction page')
    st.sidebar.write('Predict whether a customer will churn or not')
    pipeline = load_pipline()


    #load models in 

    models_paths ={
        'Logistic Regression': 'models/LR_model.pkl',
        'XGBoost': 'models/XB_model.pkl',
        'SVC': 'models/SVC_model.pkl',
        
    }

    model_choice = st.selectbox('Select a Model',list(models_paths.keys()))
    model= load_model(models_paths[model_choice])

    if model is None:
        st.error('Failed to load model')
        return
    
    #check the model type

    st.write(f'Loaded model type: {type(model)}')

    #Single Prediction
    st.subheader("Single Customer Prediction")
    gender = st.selectbox("Gender", ['Male', 'Female'])
    senior_citizen = st.selectbox("Senior Citizen", ['Yes', 'No'])
    partner = st.selectbox("Partner", ['Yes', 'No'])
    dependents = st.selectbox("Dependents", ['Yes', 'No'])
    tenure = st.slider("Tenure (Months)", min_value=1, max_value=72, value=12)
    paperless_billing = st.selectbox("Paperless Billing", ['Yes', 'No'])
    payment_method = st.selectbox("Payment Method", ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'])
    monthly_charges = st.number_input("Monthly Charges", min_value=0.0, value=50.0)
    total_charges = st.number_input("Total Charges", min_value=0.0, value=500.0)
    phone_service = st.selectbox("Phone Service", ['Yes', 'No'])
    multiple_lines = st.selectbox("Multiple Lines", ['Yes', 'No', 'No phone service'])
    internet_service = st.selectbox("Internet Service", ['DSL', 'Fiber optic', 'No'])
    online_security = st.selectbox("Online Security", ['Yes', 'No', 'No internet service'])
    online_backup = st.selectbox("Online Backup", ['Yes', 'No', 'No internet service'])
    device_protection = st.selectbox("Device Protection", ['Yes', 'No', 'No internet service'])
    tech_support = st.selectbox("Tech Support", ['Yes', 'No', 'No internet service'])
    streaming_tv = st.selectbox("Streaming TV", ['Yes', 'No', 'No internet service'])
    streaming_movies = st.selectbox("Streaming Movies", ['Yes', 'No', 'No internet service'])
    contract = st.selectbox("Contract", ['Month-to-month', 'One year', 'Two year'])

    #predict for a single customer
    if st.button('Predict Single'):

        data = pd.DataFrame({'gender' :[gender],
    'senior_citizen' : [senior_citizen],
    'partner' :[partner],
    'dependents' :[dependents],
    'tenure' :[tenure],
    'paperless_billing' :[paperless_billing],
    'payment_method' :[payment_method],
    'monthly_charges' :[monthly_charges],
    'total_charges' :[ total_charges],
    'phone_service' :[phone_service],
    'multiple_lines' :[multiple_lines],
    'internet_service': [internet_service],
    'online_security' :[online_security],
    'online_backup' : [online_backup],
    'device_protection' : [device_protection],
    'tech_support' :[tech_support],
    'streaming_tv' : [streaming_tv],
    'streaming_movies' : [streaming_movies],
    'contract' : [contract]
    })
    

    prediction = pipeline.predict(data)[0]
    probability = pipeline.predict_proba(data)[0][1]* 100

    #display result
    st.write(f"Single Prediction: {'Churn' if prediction == 1 else 'Not Churn'}")
    st.write(f'Churned Probability : {probability: .2f}%')
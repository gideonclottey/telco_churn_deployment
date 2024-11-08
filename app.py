import streamlit as st
from streamlit_option_menu import option_menu
from home import home_page
from data import data_page
from predict import predict_page
from dashboard import dashboard_page
from auth import authenticate

def main():
    authenticate()
    if st.session_state.authenticated:
        with st.sidebar:
            page = option_menu(
            menu_title= 'Main Menu',
            options=['Home','Data', 'Predict', 'Dashboard'],
            icons=['house','table',"graph-up-arrow","speedometer"],
            default_index= 0
        )


        if page == "Home":
            home_page()
        elif page == "Data":
            data_page()
        elif page == "Predict":
            predict_page()
        elif page == "Dashboard":
            dashboard_page()

if __name__ == "__main__":
    main()

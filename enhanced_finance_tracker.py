# File: enhanced_finance_tracker.py

import streamlit as st
import importlib
from auth.auth import authenticate, create_user

def main():
    # Set background colors and font style for main page and sidebar
    st.markdown(
        """
        <style>
        .main {
            background-color: #1a1a1a;  /* Dark background for contrast */
            color: #ffffff;  /* White font color for readability */
        }
        .sidebar .sidebar-content {
            background-color: #333333;  /* Darker sidebar background */
        }
        body {
            font-family: 'Arial', sans-serif;
            font-weight: bold;
            text-transform: uppercase;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("Enhanced Finance Tracker")
    
    if 'logged_in' not in st.session_state or not st.session_state['logged_in']:
        st.header("Please Log In")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        
        if st.button("Login"):
            if authenticate(username, password):
                st.session_state.logged_in = True
                st.session_state.username = username
                st.success("Logged in successfully!")
            else:
                st.error("Invalid username or password")

        if st.button("Create Account"):
            if create_user(username, password):
                st.success("Account created successfully!")
            else:
                st.error("User already exists or invalid password")
        return

    if st.button('Logout'):
        st.session_state.pop('username', None)
        st.session_state.pop('logged_in', None)
        st.experimental_rerun()

    # Define page sequence
    PAGES = {
        "Enhanced Finance Tracker": "pages.home",
        "Home": "pages.home",
        "Budget Overview": "pages.budget_overview",
        "Historical Data": "pages.historical_data",
        "Export Data": "pages.export_data"
    }

    # Create sidebar for page navigation
    selection = st.sidebar.radio("Go to", [
        "Enhanced Finance Tracker",
        "Home",
        "Budget Overview",
        "Historical Data",
        "Export Data"
    ])
    
    module_name = PAGES[selection]
    module = importlib.import_module(f'{module_name.replace(".py", "")}')
    module.main()

if __name__ == "__main__":
    main()

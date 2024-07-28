import streamlit as st
import importlib
from auth import authenticate, create_user

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
    st.subheader("Empowering Your Financial Journey with Clarity and Control")

    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False

    if not st.session_state['logged_in']:
        st.header("Please Log In")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login", key="login_button"):
            if authenticate(username, password):
                st.session_state.logged_in = True
                st.session_state.username = username
                st.success("Logged in successfully!")
            else:
                st.error("Invalid username or password")

        if st.button("Create Account", key="create_account_button"):
            if create_user(username, password):
                st.success("Account created successfully!")
            else:
                st.error("User already exists or invalid password")
    else:
        if st.button('Logout', key="logout_button"):
            st.session_state['logged_in'] = False
            st.session_state.pop('username', None)
            st.success("Logged out successfully!")

        # Create sidebar for page navigation
        selection = st.sidebar.radio("Go to", [
            "Enhanced Finance Tracker",
            "Home",
            "Budget Overview",
            "Historical Data",
            "Export Data"
        ])

        PAGES = {
            "Enhanced Finance Tracker": "enhanced_finance_tracker",
            "Home": "home",
            "Budget Overview": "budget_overview",
            "Historical Data": "historical_data",
            "Export Data": "export_data"
        }

        module_name = PAGES.get(selection)
        if module_name:
            module = importlib.import_module(f'{module_name}')
            if hasattr(module, 'main'):
                module.main()
            else:
                st.error(f"Module {module_name} does not have a 'main' function.")
        else:
            st.error("Page not found")

if __name__ == "__main__":
    main()

import streamlit as st
import pandas as pd
from auth.user_data import load_user_data

# Define consistent styles for all pages
st.markdown("""
    <style>
    /* Set global font style */
    * {
        font-family: 'Arial', sans-serif;
        font-weight: bold;
        text-transform: uppercase;
    }
    /* Set sidebar font and background */
    .css-1d391kg {
        font-size: 18px;
        background-color: #333;
        color: #ddd;
    }
    </style>
    """, unsafe_allow_html=True)


def main():
    if 'logged_in' not in st.session_state or not st.session_state.logged_in:
        st.error("Please log in to access this page.")
        return

    st.title("Export Data")

    # Load user data
    username = st.session_state.get("username")
    if username:
        data = load_user_data(username)
        st.write("Here is your data:")
        st.write(data)

        # Button to export data to CSV
        if st.button("Export to CSV"):
            data.to_csv(f"{username}_export.csv", index=False)
            st.success(f"Data exported as {username}_export.csv!")
    else:
        st.error("No user data found.")

if __name__ == "__main__":
    main()
import streamlit as st
import pandas as pd
from auth.user_data import load_user_data, save_user_data

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
    /* Set sidebar text style */
    .css-1n543e5 p {
        font-family: 'Arial', sans-serif;
        font-weight: bold;
        text-transform: uppercase;
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    st.title("Home")
    st.markdown("<style>body { font-family: 'Arial', sans-serif; font-weight: bold; text-transform: uppercase; background-color: #1a1a1a; color: #ffffff; }</style>", unsafe_allow_html=True)

    if 'username' not in st.session_state:
        st.error("You must be logged in to access this page.")
        return

    username = st.session_state.username
    data = load_user_data(username)

    st.header('Add a New Entry')
    data_type = st.selectbox('Type', ['Income', 'Expense'])
    category = st.selectbox('Category', ['Salary', 'Bonus', 'Other'] if data_type == 'Income' else ['Food', 'Rent', 'Utilities', 'Transportation', 'Entertainment', 'Other'])
    amount = st.number_input('Amount', min_value=0.0, step=0.01)
    date = st.date_input('Date', pd.to_datetime('today'))

    if st.button('Add Entry'):
        if category and amount > 0:
            new_entry = pd.DataFrame({'Type': [data_type], 'Category': [category], 'Amount': [amount], 'Date': [date]})
            data = pd.concat([data, new_entry], ignore_index=True)
            save_user_data(username, data)
            st.success('Entry added!')
        else:
            st.error('Please provide a valid category and amount.')

    st.write("User-specific data:")
    st.write(data)

if __name__ == "__main__":
    main()

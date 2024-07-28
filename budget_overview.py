import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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


def load_user_data(user_id):
    # Dummy implementation for demonstration purposes
    # Replace this with actual logic to load data from a database or file
    data = {
        1: pd.DataFrame({
            'Type': ['Income', 'Expense', 'Expense', 'Expense', 'Income', 'Expense', 'Income'],
            'Category': ['Salary', 'Rent', 'Utilities', 'Food', 'Bonus', 'Transportation', 'Other'],
            'Amount': [5000, 1200, 300, 400, 1500, 100, 2000]
        }),
        2: pd.DataFrame({
            'Type': ['Income', 'Expense', 'Expense', 'Expense', 'Income', 'Expense'],
            'Category': ['Consulting', 'Rent', 'Utilities', 'Groceries', 'Interest', 'Car'],
            'Amount': [4000, 1000, 250, 350, 200, 300]
        })
    }
    return data.get(user_id, pd.DataFrame(columns=['Type', 'Category', 'Amount']))

def display_budget_overview():
    if 'logged_in' not in st.session_state or not st.session_state['logged_in']:
        st.error("Please log in to access this page.")
        return

    st.title("Budget Overview")

    # Assuming you have the logged-in user's ID stored in session state
    user_id = st.session_state.get('user_id', 1)  # Default to 1 for testing purposes

    # Load user-specific data
    user_data = load_user_data(user_id)

    if user_data.empty:
        st.warning("No data available for this user.")
        return

    # Separate income and expense data
    expense_data = user_data[user_data['Type'] == 'Expense']
    income_data = user_data[user_data['Type'] == 'Income']

    # Pie chart of expenses
    st.subheader("Expenses Breakdown")
    fig1, ax1 = plt.subplots()
    ax1.pie(expense_data['Amount'], labels=expense_data['Category'], autopct='%1.1f%%')
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig1)

    # Bar chart of incomes
    st.subheader("Incomes Breakdown")
    fig2, ax2 = plt.subplots()
    ax2.bar(income_data['Category'], income_data['Amount'], color='green')
    ax2.set_xlabel('Income Category')
    ax2.set_ylabel('Amount')
    ax2.set_title('Income Bar Chart')
    st.pyplot(fig2)

if __name__ == "__main__":
    display_budget_overview()
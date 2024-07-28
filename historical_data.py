import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

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

    st.title("Historical Data")
    
    # Sample data
    data = pd.DataFrame({
        'Type': ['Income', 'Expense', 'Expense', 'Expense', 'Expense', 'Income', 'Income', 'Income'],
        'Category': ['Salary', 'Rent', 'Transportation', 'Entertainment', 'Utilities', 'Bonus', 'Other', 'Other'],
        'Amount': [25000, 5000, 1000, 1000, 2000, 10000, 50000, 50000],
        'Date': pd.to_datetime(['2024-07-28', '2024-07-28', '2024-07-28', '2024-07-28', '2024-07-26', '2024-07-25', '2024-07-28', '2023-07-14'])
    })
    
    st.write(data)

    # Filter data by type
    income_data = data[data['Type'] == 'Income']
    expense_data = data[data['Type'] == 'Expense']

    # Plotting
    fig, ax = plt.subplots()

    ax.plot(income_data['Date'], income_data['Amount'].cumsum(), label='Income', marker='o')
    ax.plot(expense_data['Date'], expense_data['Amount'].cumsum(), label='Expense', marker='o')
    
    ax.set_xlabel('Date')
    ax.set_ylabel('Cumulative Amount')
    ax.set_title('Cumulative Income and Expense Over Time')
    ax.legend()

    # Show plot
    st.pyplot(fig)

if __name__ == "__main__":
    main()
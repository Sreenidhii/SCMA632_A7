import os
import pandas as pd

def get_user_data_path(username):
    return f"{username}_data.csv"

def load_user_data(username):
    path = get_user_data_path(username)
    if os.path.isfile(path):
        return pd.read_csv(path)
    return pd.DataFrame(columns=['Type', 'Category', 'Amount', 'Date'])

def save_user_data(username, data):
    path = get_user_data_path(username)
    data.to_csv(path, index=False)

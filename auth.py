# File: auth/auth.py

import hashlib

# Simple in-memory user store (this should be replaced with a database)
users_db = {
    "admin": hashlib.sha256("password".encode()).hexdigest()  # Pre-created user
}

def hash_password(password):
    """Hash a password for storing."""
    return hashlib.sha256(password.encode()).hexdigest()

def authenticate(username, password):
    """Authenticate a user."""
    if not password:  # Check if password is empty
        return False
    hashed_pw = hash_password(password)
    return username in users_db and users_db[username] == hashed_pw

def create_user(username, password):
    """Create a new user."""
    if not password:  # Ensure a password is provided
        return False
    if username in users_db:
        return False
    users_db[username] = hash_password(password)
    return True

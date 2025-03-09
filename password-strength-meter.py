import streamlit as st
import re
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def check_strength(password):
    strength = 0
    remarks = []

    # Length Checker
    if len(password) >= 8:
        strength += 1
    else:
        remarks.append("Password should be at least 8 characters.")

    # Uppercase Checker
    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        remarks.append("Add at least one uppercase letter.")

    # Lowercase Checker
    if re.search(r'[a-z]', password):
        strength += 1
    else:
        remarks.append("Add at least one lowercase letter.")

    # Number Checker
    if re.search(r'[0-9]', password):
        strength += 1
    else:
        remarks.append("Include at least one number.")

    # Special Character Checker
    if re.search(r'[@$!%*?&]', password):
        strength += 1
    else:
        remarks.append("Include at least one special character (@$!%*?&).")

    return strength, remarks

# Streamlit UI
st.title("🔐 Password Strength Meter")

password = st.text_input("Enter Password:", type="password")

if password:
    strength, feedback = check_strength(password)

    # Strength Meter Bar
    st.progress(strength / 5) 

    # Color-coded Strength Label
    if strength == 5:
        st.success("Strong Password 💪")
    elif strength >= 3:
        st.warning("Moderate Password ⚠️")
    else:
        st.error("Weak Password 🚨")

    # Suggestions
    if feedback:
        st.write("🔹 **Suggestions:**")
        for remark in feedback:
            st.write(f"- {remark}")


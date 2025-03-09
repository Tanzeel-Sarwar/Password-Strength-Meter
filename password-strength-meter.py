import streamlit as st
import re

# Function to check password strength
def check_strength(password):
    strength = 0
    remarks = []

    # Strength Criteria
    if len(password) >= 8:
        strength += 1
    else:
        remarks.append("🔴 Password should be at least **8 characters**.")

    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        remarks.append("🟠 Add at least **one uppercase letter** (A-Z).")

    if re.search(r'[a-z]', password):
        strength += 1
    else:
        remarks.append("🟡 Add at least **one lowercase letter** (a-z).")

    if re.search(r'[0-9]', password):
        strength += 1
    else:
        remarks.append("🔵 Include at least **one number** (0-9).")

    if re.search(r'[@$!%*?&]', password):
        strength += 1
    else:
        remarks.append("🟣 Include at least **one special character** (@$!%*?&).")

    return strength, remarks

# Streamlit UI
st.set_page_config(page_title="Password Strength Meter", page_icon="🔐", layout="centered")

# Custom Styling
st.markdown(
    """
    <style>
    .big-font { font-size:22px !important; font-weight: bold; }
    .center { text-align: center; }
    </style>
    """, unsafe_allow_html=True
)

st.markdown("<h1 class='center'>🔐 Password Strength Meter</h1>", unsafe_allow_html=True)
st.write("👀 Enter a password below to check its strength and get recommendations.")

# Password Input
password = st.text_input("Enter Password:", type="password")

if password:
    strength, feedback = check_strength(password)

    # Strength bar with colors
    strength_labels = ["❌ Very Weak", "⚠️ Weak", "😐 Moderate", "👍 Good", "💪 Strong"]
    strength_colors = ["red", "orange", "yellow", "blue", "green"]

    st.markdown(f"### **Strength: {strength_labels[strength]}**", unsafe_allow_html=True)
    st.progress(strength / 5)  # Normalized (0 to 1)

    # Show suggestions for improvement
    if feedback:
        st.markdown("### 🔍 **Suggestions to Improve Password:**")
        for remark in feedback:
            st.write(f"- {remark}")

    # Password visibility toggle
    if st.checkbox("👁 Show Password"):
        st.write(f"🔑 Your Password: `{password}`")


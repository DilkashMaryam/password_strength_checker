"""A Streamlit web application for checking password strength and providing feedback."""

import re
import streamlit as st

#page styling
st.set_page_config(
    page_title="Password strength checker",
    page_icon=":🔒:",
    layout="centered"
)

#custom css
st.markdown("""
<style>
    .main {text-align: center;
    .stTextInput {width: 60% !important; margin: auto;}
    .stButton button{width: 50%; background-color: #000; color: #fff; border-radius: 5px; font-size: 18px; padding: 10px; margin: 20px 0;}
    .stButton button:hover{background-color: #333;}
</style>
""", unsafe_allow_html=True)

#title
st.title("Password strength checker by Dilkash Maryam🌸")

#password input
st.write("Enter your password to check its security level.🔍")

#function to check password strength
def check_password_strength(password):
    """Evaluate password strength based on length, case, numbers and special characters."""
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append(" ❌ Password is too short. It should be **at least 8 characters long**.")

    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append(" ❌ Password should contain **at least one uppercase letter and one lowercase letter**.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append(" ❌ Password should contain **at least one number**.")

    if re.search(r"[!@#$%^&*()]", password):
        score += 1
    else:
        feedback.append(" ❌ Password should contain **at least one special character**.")

#dislay password strength result
    if score == 4:
        st.success("😃**Strong password!**. Your password is secure and meets all the required criteria.")
    elif score == 3:
        st.warning("😊**Good password!**. Your password is fairly secure but could be improved.")
    else:
        st.error("😓**Weak password!**. Your password is not secure. Please make it stronger.")

    #feedback
    if feedback:
        with st.expander("🔍**Password hints:**"):
            for suggestion in feedback:
                st.write(suggestion)

#password input
user_password = st.text_input(
    "Enter your password:",
    type="password",
    help="Password should be at least 8 characters long and contain at least one "
    "uppercase letter, one lowercase letter, one number, and one special character."
)

#Button to check password strength
if st.button("Check password strength"):
    if user_password:
        check_password_strength(user_password)
    else:
        st.warning("⚠️Please enter a password to check its strength.")

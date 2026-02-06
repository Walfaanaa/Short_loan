# ==============================
# EGSA Short Loan - Streamlit App
# Mobile-Friendly Version
# ==============================

import streamlit as st
from datetime import date

# ------------------------------
# PAGE CONFIG
# ------------------------------
st.set_page_config(
    page_title="EGSA Short Loan",   # This controls the name on mobile install
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ------------------------------
# HIDE STREAMLIT DEFAULT UI
# ------------------------------
st.markdown("""
<style>
/* Hide Streamlit header & footer */
header {visibility: hidden;}
footer {visibility: hidden;}

/* Optional: Make app full width on mobile */
.css-18e3th9 {padding-top: 1rem;}
</style>
""", unsafe_allow_html=True)

# ------------------------------
# APP LOGIC STARTS HERE
# ------------------------------

st.title("EGSA Short Loan App 📱")

st.write("Welcome to the Short-Term Loan Management App for EGSA members!")

# Example: Input loan data
name = st.text_input("Enter your name")
loan_amount = st.number_input("Loan Amount", min_value=0.0, value=1000.0, step=100.0)
interest_rate = st.number_input("Interest Rate (%)", min_value=0.0, value=10.0, step=0.5)
due_days = st.number_input("Loan duration (days)", min_value=1, value=30, step=1)

# Calculate due date and interest
if st.button("Calculate Loan"):
    interest_amount = loan_amount * (interest_rate / 100)
    total_amount = loan_amount + interest_amount
    due_date = date.today().toordinal() + due_days
    due_date = date.fromordinal(due_date)
    
    st.write(f"Loan for: **{name}**")
    st.write(f"Principal: **{loan_amount:.2f}**")
    st.write(f"Interest ({interest_rate}%): **{interest_amount:.2f}**")
    st.write(f"Total to pay: **{total_amount:.2f}**")
    st.write(f"Due date: **{due_date}**")

# Optional: Footer
st.markdown("---")
st.markdown("EGSA Short Loan App - Mobile Friendly Version")

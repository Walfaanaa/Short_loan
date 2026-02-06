# ==============================
# EGSA Short Loan - Streamlit App
# Mobile-Friendly Version
# ==============================

import streamlit as st
from datetime import date, timedelta

# ------------------------------
# PAGE CONFIG
# ------------------------------
st.set_page_config(
    page_title="EGSA Short Loan",   # Mobile app name
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ------------------------------
# HIDE STREAMLIT DEFAULT UI
# ------------------------------
st.markdown("""
<style>
header {visibility: hidden;}
footer {visibility: hidden;}
.css-18e3th9 {padding-top: 1rem;}
</style>
""", unsafe_allow_html=True)

# ------------------------------
# APP LOGIC STARTS HERE
# ------------------------------

st.title("EGSA Short Loan App 📱")
st.write("Welcome to the Short-Term Loan Management App for EGSA members!")

# ------------------------------
# LOAN OPTIONS
# ------------------------------

# Predefined loan amounts
loan_options = {
    2000: 5,    # Amount: interest %
    5000: 5,
    10000: 10,
    15000: 15
}

# Predefined durations (days)
duration_options = [7, 15, 30, 60]

# User selects loan amount
loan_amount = st.selectbox("Select Loan Amount", options=list(loan_options.keys()))

# Automatically set interest rate
interest_rate = loan_options[loan_amount]
st.write(f"Interest Rate: **{interest_rate}%**")

# User selects duration
duration_days = st.selectbox("Select Loan Duration (days)", options=duration_options)

# User enters name
name = st.text_input("Enter your name")

# ------------------------------
# CALCULATE LOAN
# ------------------------------
if st.button("Calculate Loan"):

    # Calculate interest and total
    interest_amount = loan_amount * (interest_rate / 100)
    total_amount = loan_amount + interest_amount

    # Calculate due date
    due_date = date.today() + timedelta(days=duration_days)

    # Display results
    st.markdown("### Loan Details")
    st.write(f"Name: **{name}**")
    st.write(f"Principal: **{loan_amount:.2f}**")
    st.write(f"Interest ({interest_rate}%): **{interest_amount:.2f}**")
    st.write(f"Total to Pay: **{total_amount:.2f}**")
    st.write(f"Due Date: **{due_date}** days from today ({duration_days} days)")

# Optional Footer
st.markdown("---")
st.markdown("EGSA Short Loan App - Mobile Friendly Version")

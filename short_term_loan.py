# ==============================
# EGSA Short Loan - Mobile Friendly
# With Auto Penalty
# ==============================

import streamlit as st
from datetime import date, timedelta

# ------------------------------
# PAGE CONFIG
# ------------------------------
st.set_page_config(
    page_title="EGSA Short Loan",
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
# APP TITLE
# ------------------------------
st.title("EGSA Short Loan App 📱")
st.write("Quick loan calculator for EGSA members with automatic penalty.")

# ------------------------------
# LOAN OPTIONS
# ------------------------------
loan_options = {
    2000: 5,     # Amount: interest %
    5000: 5,
    10000: 10,
    15000: 15
}

duration_options = {
    2000: 7,     # default durations in days
    5000: 15,
    10000: 30,
    15000: 60
}

# User selects loan amount
loan_amount = st.selectbox("Select Loan Amount", options=list(loan_options.keys()))
interest_rate = loan_options[loan_amount]
st.write(f"Interest Rate: **{interest_rate}%**")

# Automatically assign duration
loan_duration = duration_options[loan_amount]
st.write(f"Loan Duration: **{loan_duration} days**")

# User enters name
name = st.text_input("Enter your name")

# ------------------------------
# PAY DATE INPUT
# ------------------------------
pay_date = st.date_input("Select Payment Date (leave empty if paying today)", value=date.today())

# ------------------------------
# CALCULATE LOAN
# ------------------------------
if st.button("Calculate Loan"):

    # Calculate interest
    interest_amount = loan_amount * (interest_rate / 100)
    total_amount = loan_amount + interest_amount

    # Due date
    due_date = date.today() + timedelta(days=loan_duration)

    # Check for penalty
    if pay_date > due_date:
        penalty = total_amount * 0.10  # 10% penalty
        total_with_penalty = total_amount + penalty
        st.warning(f"⚠️ Payment is late! 10% penalty applied: **{penalty:.2f}**")
    else:
        penalty = 0
        total_with_penalty = total_amount
        st.success("✅ Payment on time. No penalty applied.")

    # Display results
    st.markdown("### Loan Details")
    st.write(f"Name: **{name}**")
    st.write(f"Principal: **{loan_amount:.2f}**")
    st.write(f"Interest ({interest_rate}%): **{interest_amount:.2f}**")
    st.write(f"Total to Pay: **{total_amount:.2f}**")
    st.write(f"Due Date: **{due_date}**")
    if penalty > 0:
        st.write(f"Total with Penalty (10%): **{total_with_penalty:.2f}**")
    else:
        st.write(f"Total Amount to Pay: **{total_with_penalty:.2f}**")

# Footer
st.markdown("---")
st.markdown("EGSA Short Loan App - Mobile Friendly Version")

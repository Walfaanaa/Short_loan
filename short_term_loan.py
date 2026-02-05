import streamlit as st
from PIL import Image
import requests
from datetime import date, timedelta

# =======================
# Top Center Logo
# =======================
logo_url = "https://raw.githubusercontent.com/Walfaanaa/Short_loan/main/EGSA.png"
response = requests.get(logo_url, stream=True)
logo = Image.open(response.raw)

col1, col2, col3 = st.columns([2, 1, 2])
with col2:
    st.image(logo, use_container_width=True)

st.markdown("<h2 style='text-align:center;'>Short Term Loan Calculator</h2>", unsafe_allow_html=True)
st.write("")

# =======================
# Loan Levels
# =======================
loan_levels = {
    2000: {"interest_rate": 0.05, "due_days": 7},
    5000: {"interest_rate": 0.05, "due_days": 15},
    10000: {"interest_rate": 0.10, "due_days": 30},
    15000: {"interest_rate": 0.15, "due_days": 60}
}

st.write("### Enter Loan Details")

loan_amount = st.selectbox(
    "Select Loan Amount",
    list(loan_levels.keys())
)

# =======================
# Date Inputs
# =======================
business_date = st.date_input(
    "Business Date (Loan Taken Date)",
    value=date.today()
)

interest_rate = loan_levels[loan_amount]["interest_rate"]
due_days = loan_levels[loan_amount]["due_days"]

# Auto due date (for reference only)
due_date = business_date + timedelta(days=due_days)

# 🔹 Manual Late Days Entry
late_days = st.number_input(
    "Late Days (Enter number of days after due date)",
    min_value=0,
    step=1,
    value=0
)

# =======================
# Calculations
# =======================
interest = loan_amount * interest_rate
total_due = loan_amount + interest

# Penalty: 10% of loan amount per day late
penalty_per_day = loan_amount * 0.10
total_penalty = late_days * penalty_per_day

final_amount = total_due + total_penalty

# =======================
# Results
# =======================
st.write("## 📊 Loan Summary")

st.success(f"Loan Amount: {loan_amount:,.2f}")
st.info(f"Interest Rate: {interest_rate*100:.0f}%")
st.info(f"Due Days: {due_days} days")

st.write(f"📅 **Business Date:** {business_date}")
st.write(f"📅 **Due Date (Auto):** {due_date}")

st.write(f"Interest Amount: {interest:,.2f}")
st.write(f"Total Due (Loan + Interest): {total_due:,.2f}")

st.warning(f"Late Days Entered: {late_days}")
st.warning(f"Penalty Per Day (10% of Loan): {penalty_per_day:,.2f}")
st.warning(f"Total Penalty: {total_penalty:,.2f}")

st.write("## ✅ Final Amount to Pay")
st.error(f"{final_amount:,.2f}")

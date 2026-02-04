import streamlit as st
from PIL import Image
import requests

# =======================
# Top Center Logo
# =======================
logo_url = "https://raw.githubusercontent.com/Walfaanaa/Short_loan/main/EGSA.png"
response = requests.get(logo_url, stream=True)
logo = Image.open(response.raw)

# Center the logo perfectly
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
    5000: {"interest_rate": 0.5, "due_days": 15},
    10000: {"interest_rate": 0.1, "due_days": 30},
    15000: {"interest_rate": 0.20, "due_days": 60}
}

st.write("### Enter Loan Details")

loan_amount = st.selectbox("Select Loan Amount", [2000,5000, 10000, 15000])
days_passed = st.number_input("Number of days since loan taken", min_value=0, step=1)

# =======================
# Calculations
# =======================
interest_rate = loan_levels[loan_amount]["interest_rate"]
due_days = loan_levels[loan_amount]["due_days"]

interest = loan_amount * interest_rate
total_due = loan_amount + interest

late_days = max(0, days_passed - due_days)

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

st.write(f"Interest Amount: {interest:,.2f}")
st.write(f"Total Due (Loan + Interest): {total_due:,.2f}")

st.warning(f"Late Days: {late_days}")
st.warning(f"Penalty Per Day (10% of Loan): {penalty_per_day:,.2f}")
st.warning(f"Total Penalty: {total_penalty:,.2f}")

st.write("## ✅ Final Amount to Pay")
st.error(f"{final_amount:,.2f}")






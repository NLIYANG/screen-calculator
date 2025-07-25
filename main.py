import streamlit as st

# Title
st.title("📱 Screen Time Calculator for Kids")

# Input: Name
name = st.text_input("What's your name?")

# Input: Hours of screen time per day
hours_per_day = st.number_input("How many hours do you spend on screens per day?", min_value=0.0, max_value=24.0, step=0.5)

# Calculation and Output
if name and hours_per_day > 0:
    days_per_week = round((hours_per_day * 7) / 24, 2)
    weeks_per_year = round((hours_per_day * 365) / (24 * 7), 2)
    years_in_lifetime = round((hours_per_day * 365 * 70) / (24 * 365), 2)  # Simplifies to hours_per_day * 70 / 24

    st.markdown(f"### 👋 Hi {name}!")
    st.markdown(f"At **{hours_per_day} hours** of screen time per day:")
    st.markdown(f"- You will spend **{days_per_week} full days** on screens every week.")
    st.markdown(f"- That adds up to **{weeks_per_year} weeks** per year.")
    st.markdown(f"- Over a lifetime (up to 70 years), that's **{years_in_lifetime} years** spent looking at screens.")

    st.info("📵 Imagine what else you could do with those years!")

elif name and hours_per_day == 0:
    st.markdown(f"Great job, {name}! No screen time today? 🎉 Keep it up!")

# Optional: Footer
st.markdown("---")
st.caption("Created to help kids understand the importance of screen time balance. 👀💡")

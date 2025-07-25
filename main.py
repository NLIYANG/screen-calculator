import streamlit as st
import time

# Minimalist Style
st.set_page_config(page_title="Screen Time Steward", layout="centered")

# Function to simulate progressive text reveal
def typewriter(message, delay=0.1):
    for word in message.split():
        st.markdown(f"### {word} ", unsafe_allow_html=True)
        time.sleep(delay)

# Welcome Section
st.title("📱 Screen Time Steward")

# Show text progressively (simulating a conversation)
if 'show_intro' not in st.session_state:
    st.session_state.show_intro = True

if st.session_state.show_intro:
    with st.empty():
        typewriter("Let's", 0.2)
        time.sleep(0.3)
        typewriter("see", 0.2)
        time.sleep(0.3)
        typewriter("how", 0.2)
        time.sleep(0.3)
        typewriter("much", 0.2)
        time.sleep(0.3)
        typewriter("time", 0.2)
        time.sleep(0.3)
        typewriter("you", 0.2)
        time.sleep(0.3)
        typewriter("spend", 0.2)
        time.sleep(0.3)
        typewriter("on", 0.2)
        time.sleep(0.3)
        typewriter("your", 0.2)
        time.sleep(0.3)
        typewriter("phone...", 0.2)
        time.sleep(1.5)
        st.session_state.show_intro = False
        st.rerun()

# Bible Verse on Stewardship
st.markdown("---")
st.markdown("📖 **Ephesians 5:15-16**  
*“Look carefully then how you walk, not as unwise but as wise, making the best use of the time, because the days are evil.”*")

# Input Section
st.markdown("---")
name = st.text_input("👋 What's your name?")
hours_per_day = st.slider("⏰ How many hours do you spend on screens per day?", 0.0, 24.0, 1.0, step=0.5)

# Output Section
if name and hours_per_day > 0:
    days_per_week = round((hours_per_day * 7) / 24, 2)
    weeks_per_year = round((hours_per_day * 365) / (24 * 7), 2)
    years_in_lifetime = round((hours_per_day * 70) / 24, 2)

    st.markdown(f"### 👋 Hi **{name}**!")
    st.success(f"At **{hours_per_day} hours** per day, that means:")
    st.markdown(f"- 📅 **{days_per_week} full days** per week")
    st.markdown(f"- 🗓 **{weeks_per_year} weeks** every year")
    st.markdown(f"- 🧓 **{years_in_lifetime} years** over your lifetime (if you live to 70)")

    st.info("⏳ Time is a gift—how will you use it wisely?")

elif name and hours_per_day == 0:
    st.balloons()
    st.success(f"Way to go, {name}! No screen time today! 🎉")

# Footer
st.markdown("---")
st.caption("Built to help kids reflect on time and stewardship 📱🕊")

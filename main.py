import streamlit as st
import time

# Set page config
st.set_page_config(page_title="Screen Time Steward", layout="centered")

# Show welcome screen on first load
if "show_intro" not in st.session_state:
    st.session_state.show_intro = True
    st.session_state.intro_time = time.time()

if st.session_state.show_intro:
    st.markdown("## 👋 Welcome!")
    st.markdown("### Let's find out how much time you spend on your phone or tablet 📱")
    st.markdown("### And see what that looks like over your whole life ⏳")
    st.markdown("---")
    st.markdown("""
    📖 **Ephesians 5:15-16**  
    *“Look carefully then how you walk, not as unwise but as wise, making the best use of the time, because the days are evil.”*
    """)
    
    # Wait 3 seconds then switch to main app
    if time.time() - st.session_state.intro_time > 3:
        st.session_state.show_intro = False
        st.experimental_rerun()
    else:
        st.stop()

# === Main App ===
st.title("📱 Screen Time Calculator")

name = st.text_input("👶 What's your name?")
hours_per_day = st.slider("⏰ How many hours do you spend on screens per day?", 0.0, 24.0, 1.0, step=0.5)

if name and hours_per_day > 0:
    days_per_week = round((hours_per_day * 7) / 24, 2)
    weeks_per_year = round((hours_per_day * 365) / (24 * 7), 2)
    years_in_lifetime = round((hours_per_day * 70) / 24, 2)

    st.markdown(f"### Hi **{name}**!")
    st.success(f"At **{hours_per_day} hours** per day, that means:")
    st.markdown(f"- 📅 **{days_per_week} full days** per week")
    st.markdown(f"- 🗓 **{weeks_per_year} weeks** every year")
    st.markdown(f"- 🧓 **{years_in_lifetime} years** in your lifetime (70 years)")

    st.info("⏳ Time is a gift. Use it wisely!")
elif name and hours_per_day == 0:
    st.balloons()
    st.success(f"Way to go, {name}! No screen time today! 🎉")

st.markdown("---")
st.caption("Built to help kids reflect on time and stewardship 📱🕊")

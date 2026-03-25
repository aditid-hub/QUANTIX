import streamlit as st
import os
import sys
from datetime import date, datetime

# 1. Path fix
sys.path.append(os.getcwd())

# 2. Imports
from core.load_engine import predict_priority
from utils.file_handler import save_to_json, load_from_json

# --- Page Config ---
st.set_page_config(page_title="QUANTIX", layout="wide")

# ==========================================================
#                  HEADER SECTION
# ==========================================================
h1, h2, h3 = st.columns([1, 2, 1])
with h2:
    st.image("https://images.unsplash.com/photo-1484480974693-6ca0a78fb36b?q=80&w=2072")

st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&display=swap" rel="stylesheet">
<div style="
    background: rgba(255, 255, 255, 0.03);
    backdrop-filter: blur(12px);
    border-radius: 30px;
    padding: 30px;
    text-align: center;
    margin-bottom: 20px;
    border: 1px solid rgba(220, 142, 144, 0.2);
">
    <h1 style="
        font-family: 'Dancing Script', cursive;
        color: #DC8E90;
        font-size: 85px;
        font-weight: 700;
        margin: 0;
    ">Quantix</h1>
    <p style="
        color: #E29578;
        font-family: serif;
        font-size: 16px;
        letter-spacing: 2px;
    ">A touch of intelligence</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(10px);
    text-align: center; 
    padding: 25px; 
    border-radius: 20px;
    margin: 20px 0 40px 0;
    color: #E29578; 
    font-size: 24px; 
    font-style: italic;
">
“The secret of getting ahead is getting started.”
<br>
<span style="font-size: 14px;">— Mark Twain</span>
</div>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# ==========================================================
# SESSION STATE
# ==========================================================
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = ""

# ==========================================================
# LOGIN / REGISTER
# ==========================================================
if not st.session_state.logged_in:
    tab1, tab2 = st.tabs(["Login", "Register"])

    with tab1:
        st.subheader("Login")
        user = st.text_input("Username")
        pwd = st.text_input("Password", type="password")

        if st.button("Login"):
            users = load_from_json("users.json")
            if any(u['username'] == user and u['password'] == pwd for u in users):
                st.session_state.logged_in = True
                st.session_state.username = user
                st.rerun()
            else:
                st.error("Invalid Credentials")

    with tab2:
        st.subheader("Register")
        new_user = st.text_input("New Username")
        new_pwd = st.text_input("New Password", type="password")

        if st.button("Register"):
            users = load_from_json("users.json")
            if any(u['username'] == new_user for u in users):
                st.warning("Username exists")
            else:
                users.append({"username": new_user, "password": new_pwd})
                save_to_json("users.json", users)
                st.success("Account created!")

# ==========================================================
# MAIN APP
# ==========================================================
else:
    all_tasks = load_from_json("tasks.json")
    user_tasks = [t for t in all_tasks if t.get("user") == st.session_state.username]

    # SIDEBAR
    st.sidebar.success(f"Logged in as: {st.session_state.username}")

    total_tasks = len(user_tasks)
    high_prio = len([t for t in user_tasks if t["priority"] == "High"])

    c1, c2 = st.sidebar.columns(2)
    c1.metric("Total", total_tasks)
    c2.metric("Urgent", high_prio)

    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()

    if st.sidebar.button("Clear Tasks"):
        remaining = [t for t in all_tasks if t.get("user") != st.session_state.username]
        save_to_json("tasks.json", remaining)
        st.rerun()

    # ==========================================================
    # MAIN CONTENT
    # ==========================================================
    col1, col2 = st.columns([1, 2])

    # ---------------- LEFT: ADD TASK ----------------
    with col1:
        st.subheader("➕ Add New Task")

        with st.expander("Expand to Add Task", expanded=True):
            title = st.text_input("Task Title")
            deadline = st.date_input("Deadline", min_value=date.today())
            hours = st.number_input("Hours", min_value=1)

            if st.button("Predict & Add Task"):
                if title:
                    days_left = (deadline - date.today()).days
                    if days_left <= 0:
                        days_left = 1

                    priority = predict_priority(days_left, hours)

                    tasks = load_from_json("tasks.json")

                    tasks.append({
                        "user": st.session_state.username,
                        "title": title,
                        "deadline": str(deadline),
                        "hours": hours,
                        "priority": priority
                    })

                    save_to_json("tasks.json", tasks)

                    st.success(f"Priority: {priority}")
                    st.balloons()
                    st.rerun()
                else:
                    st.error("Enter title")

    # ---------------- RIGHT: TASK LIST ----------------
    with col2:
        st.subheader("📝 Your Tasks")

        if user_tasks:
            # FIXED sorting (REAL date sorting)
            user_tasks = sorted(
                user_tasks,
                key=lambda x: datetime.strptime(x["deadline"], "%Y-%m-%d")
            )

            for t in user_tasks:
                color = "#E29578" if t["priority"] == "High" else "#83C5BE"

                st.markdown(f"""
                <div style="
                    border-left: 5px solid {color};
                    padding: 15px;
                    margin-bottom: 15px;
                    border-radius: 10px;
                    background: rgba(255,255,255,0.05);
                ">
                    <h4>{t['title']}</h4>
                    <p>Priority: <b style="color:{color}">{t['priority']}</b></p>
                    <p>Deadline: {t['deadline']} | {t['hours']} hrs</p>
                </div>
                """, unsafe_allow_html=True)

                # Overdue logic
                if datetime.strptime(t["deadline"], "%Y-%m-%d").date() < date.today():
                    st.warning("⚠️ Overdue Task")

        else:
            st.info("No tasks yet")

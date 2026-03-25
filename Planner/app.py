import streamlit as st
import os
import sys
from datetime import date

# 1. Path fix: Ensure Python can find 'core' and 'utils'
sys.path.append(os.getcwd())

# 2. Imports from your custom modules
from core.load_engine import predict_priority
from utils.file_handler import save_to_json, load_from_json

# --- 3. Page Config (Rose Gold and Charcoal Theme) ---
st.set_page_config(page_title="QUANTIX", layout="wide")

# ==========================================================
#                  AESTHETIC HEADER SECTION
# ==========================================================
# ==========================================================
#                  AESTHETIC HEADER SECTION
# ==========================================================
h1, h2, h3 = st.columns([1, 2, 1])
with h2:
    st.image("https://images.unsplash.com/photo-1484480974693-6ca0a78fb36b?q=80&w=2072")

# --- Cursive QUANTIX Style ---
st.markdown(
    """
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
            line-height: 1.2;
            text-shadow: 3px 3px 10px rgba(0,0,0,0.2);
        ">Quantix</h1>
        <p style="
            color: #E29578;
            font-family: 'serif';
            font-size: 16px;
            letter-spacing: 2px;
            margin-top: -10px;
        ">A touch of intelligence</p>
    </div>
    """,
    unsafe_allow_html=True)

# --- Glassmorphic Container for the Quote ---
st.markdown(
    """
    <div style="
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        text-align: center; 
        padding: 25px; 
        border-radius: 20px;
        margin: 20px 0 40px 0;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        color: #E29578; 
        font-family: 'serif'; 
        font-size: 28px; 
        font-style: italic;
    ">
        “The secret of getting ahead is getting started.”
        <br>
        <span style="font-size: 16px; font-weight: bold; color: #FFAFCC;">— Mark Twain</span>
    </div>
    """, 
    unsafe_allow_html=True
)

# --- Aesthetic Divider ---
st.markdown("""<hr style="height:2px;border:none;color:#E29578;background-color:#E29578;" /> """, unsafe_allow_html=True)


# ==========================================================
#                     APP STATE LOGIC
# ==========================================================
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = ""

# --- LOGIN / REGISTER SECTION ---
if not st.session_state.logged_in:
    tab1, tab2 = st.tabs(["Login", "Register"])
    
    with tab1:
        st.subheader("Login")
        user = st.text_input("Username", key="login_user")
        pwd = st.text_input("Password", type='password', key="login_pwd")
        
        if st.button("Login"):
            users = load_from_json("users.json")
            # Loop-based credential check
            if any(u['username'] == user and u['password'] == pwd for u in users):
                st.session_state.logged_in = True
                st.session_state.username = user
                # Multi-version compatible rerun
                if hasattr(st, "rerun"):
                    st.rerun()
                else:
                    st.experimental_rerun()
            else:
                st.error("Invalid Credentials")

    with tab2:
        st.subheader("Create Account")
        new_user = st.text_input("New Username")
        new_pwd = st.text_input("New Password", type='password')
        
        if st.button("Register"):
            users = load_from_json("users.json")
            if any(u['username'] == new_user for u in users):
                st.warning("Username already exists!")
            else:
                users.append({"username": new_user, "password": new_pwd})
                save_to_json("users.json", users)
                st.success("Account created! Please login.")

# ==========================================================
#                   MAIN LOGGED-IN APP
# ==========================================================
else:
    # --- 1. DATA PRE-LOADING (CRITICAL: Fixes NameError) ---
    all_tasks = load_from_json("tasks.json")
    user_tasks = [t for t in all_tasks if t.get('user') == st.session_state.username]

    # --- 2. SIDEBAR NAVIGATION ---
    st.sidebar.success(f"Logged in as: {st.session_state.username}")
    
    # Sidebar Analytics
    st.sidebar.markdown("---")
    st.sidebar.subheader("📊 Quick Stats")
    total_tasks = len(user_tasks)
    high_prio = len([t for t in user_tasks if t['priority'] == "High"])

    s1, s2 = st.sidebar.columns(2)
    s1.metric("Total Tasks", total_tasks)
    s2.metric("Urgent", high_prio)
    
    # Sidebar Tools
    st.sidebar.markdown("---")
    c1, c2 = st.sidebar.columns(2)
    with c1:
        if st.button("Logout"):
            st.session_state.logged_in = False
            if hasattr(st, "rerun"):
                st.rerun()
            else:
                st.experimental_rerun()
    with c2:
        # A simple 'admin' cleanup tool
        if st.button("Clear Tasks", help="Delete all tasks for the current user."):
            remaining_tasks = [t for t in all_tasks if t.get('user') != st.session_state.username]
            save_to_json("tasks.json", remaining_tasks)
            st.warning("All tasks cleared.")
            if hasattr(st, "rerun"):
                st.rerun()
            else:
                st.experimental_rerun()


    # --- 3. MAIN DASHBOARD CONTENT ---
    col1, col2 = st.columns([1, 2])

    with col1:
        st.subheader("➕ Add New Task")
        # Glassmorphic Form Container
        st.subheader("➕ Add New Task")
# This creates a visual border using a Markdown 'Expander' or just a simple column
with st.expander("Expand to Add Task", expanded=True):
    title = st.text_input("Task Title (e.g., Math Assignment)")
    deadline = st.date_input("Deadline", min_value=date.today())
    hours = st.number_input("Estimated Hours Needed", min_value=1, max_value=100)
    
    # ... keep the rest of your button logic here ...
            
if st.button("Predict & Add Task"):
                if title:
                    # AI FEATURE CALCULATION
                    days_left = (deadline - date.today()).days
                    if days_left <= 0: days_left = 1 # Edge case handler
                    
                    # USE THE AI MODEL
                    priority = predict_priority(days_left, hours)
                    
                    # SAVE TASK
                    # Reload to ensure we don't overwrite tasks added in another tab
                    tasks = load_from_json("tasks.json")
                    new_task = {
                        "user": st.session_state.username,
                        "title": title,
                        "deadline": str(deadline),
                        "hours": hours,
                        "priority": priority
                    }
                    tasks.append(new_task)
                    save_to_json("tasks.json", tasks)
                    st.balloons()
                    st.success(f"AI assigned **{priority}** priority!")
                    # Auto-rerun to update the task list below
                    if hasattr(st, "rerun"):
                        st.rerun()
                    else:
                        st.experimental_rerun()
                else:
                    st.error("Please enter a task title.")
with col2:
        st.subheader("📝 Your Study Schedule")
        
        if user_tasks:
            # Sort tasks by deadline (earliest first)
            user_tasks = sorted(user_tasks, key=lambda x: x['deadline'])
            
            for t in user_tasks:
                # Premium Glassmorphic Card Styling
                border_color = "#E29578" if t['priority'] == "High" else "#83C5BE"
                bg_opacity = "rgba(255, 255, 255, 0.08)" if t['priority'] == "High" else "rgba(255, 255, 255, 0.05)"
                
                st.markdown(f"""
                    <div style="
                        background: {bg_opacity};
                        backdrop-filter: blur(8px);
                        border-left: 6px solid {border_color};
                        padding: 20px;
                        border-radius: 18px;
                        margin-bottom: 20px;
                        box-shadow: 0 10px 40px 0 rgba(0, 0, 0, 0.3);
                    ">
                        <h3 style="margin:0; color: #EDF6F9; font-weight: 500;">{t['title']}</h3>
                        <p style="margin:5px 0; color: #83C5BE; font-weight: bold; font-size: 16px;">
                            Priority: <span style="color: {border_color};">{t['priority']}</span>
                        </p>
                        <div style="display: flex; justify-content: space-between; color: #BBC3C6; font-size: 14px; margin-top: 10px;">
                            <span>📅 Deadline: {t['deadline']}</span>
                            <span>⏳ Work: {t['hours']} Hours</span>
                        </div>
                    </div>
                """, unsafe_allow_html=True)
                
                # Highlight High Priority Tasks
                if t['priority'] == "High":
                    st.error("Urgent: Start this immediately!")
        else:
            st.info("Your schedule is clear. Use the sidebar to add a task!")
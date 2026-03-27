# ✍️ QUANTIX | AI-Powered Study Architect

## The Chaos of Modern Productivity
Students and professionals today are overwhelmed by "Task Inflation." When every assignment, meeting, and project is labeled "Urgent," nothing actually is. Traditional To-Do lists are static—they don't account for the relationship between the complexity of a task and the time remaining to complete it.

The Critical Gaps:
Priority Paralysis: Users spend more time deciding what to do than actually doing it because they cannot objectively calculate urgency.
Cognitive Load: Manually tracking deadlines and estimating required effort for 10+ simultaneous tasks leads to burnout and missed deadline
Uninspiring Interfaces: Most productivity tools are either overly clinical (spreadsheets) or cluttered with "bloatware," making the act of organization feel like a chore rather than a premium experience.

## The Quantix Solution
Quantix bridges the gap between raw data and actionable intelligence. By leveraging a custom logic engine, it removes the "human bias" from prioritization. It transforms a chaotic list of deadlines into a visually calibrated, glassmorphic dashboard that highlights exactly where your focus belongs—wrapped in a high-aesthetic interface that makes productivity feel like a luxury, not a burden.

**Quantix** is a high-aesthetic, intelligent task management dashboard designed for students and professionals. By combining a sleek **Rose Gold & Charcoal** glassmorphic UI with a machine learning engine, Quantix doesn't just list your tasks—it tells you what to prioritize to stay ahead.

Front Page
![WhatsApp Image 2026-03-25 at 23 56 59 (1)](https://github.com/user-attachments/assets/a246ea4a-99f0-4680-aa12-cb4aeecaad4b)
Login Page
![WhatsApp Image 2026-03-25 at 23 57 17](https://github.com/user-attachments/assets/a3044fca-7921-42ad-a3c3-22afaeba6a25)
Task Management Dashboard
![WhatsApp Image 2026-03-25 at 23 57 27](https://github.com/user-attachments/assets/22e479b7-19f7-42b7-8525-5af7f37567be)

## ✨ Key Features

*   **🧠 AI Priority Engine:** Automatically calculates task urgency (High/Medium/Low) based on deadlines and estimated workload.
*   **🧼 Glassmorphic UI:** A premium user interface featuring backdrop blurs, rose gold accents, and a custom cursive branding style.
*   **🔐 Secure Session Management:** Built-in user authentication (Login/Register) with JSON-based persistent storage.
*   **📊 Live Analytics:** Real-time sidebar metrics showing total tasks and urgent "High Priority" alerts.
*   **📅 Intelligent Scheduling:** Automatically sorts your workload by the earliest deadline to keep you on track.

## 🛠️ Tech Stack

- **Frontend:** [Streamlit](https://streamlit.io/) (Python Framework)
- **Styling:** Custom CSS & HTML Injection (Glassmorphism)
- **Backend:** Python
- **Data Storage:** JSON (File-based persistence)
- **AI/ML:** Custom `predict_priority` engine

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Streamlit

### Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/aditid-hub/quantix.git](https://github.com/aditid-hub/quantix.git)
   cd quantix

### Install dependencies:
pip install streamlit

### Project structure :
quantix/
├── main.py            # The code you provided

├── core/

│    └── load_engine.py  # AI Prediction logic

├── utils/

│   └── file_handler.py # JSON Load/Save logic

├── tasks.json         # Data storage

└── users.json         # User credentials
### Run the App:
streamlit run main.py

### Aesthetic Design
Primary Accent: #DC8E90 (Rose Gold)

Secondary Accent: #83C5BE (Seafoam Clean)

Background: Charcoal Glassmorphism (rgba(255, 255, 255, 0.05))

Typography: Custom Dancing Script cursive for branding.

### Live Demo
Experience the Quantix Dashboard live:https://aditidubey-quantix.streamlit.app/

### 📝 License
Distributed under the MIT License. See LICENSE for more information.

# “The secret of getting ahead is getting started.” — Mark Twain


# ✍️ QUANTIX | AI-Powered Study Architect

**Quantix** is a high-aesthetic, intelligent task management dashboard designed for students and professionals. By combining a sleek **Rose Gold & Charcoal** glassmorphic UI with a machine learning engine, Quantix doesn't just list your tasks—it tells you what to prioritize to stay ahead.

![WhatsApp Image 2026-03-25 at 23 56 59 (1)](https://github.com/user-attachments/assets/a246ea4a-99f0-4680-aa12-cb4aeecaad4b)
![WhatsApp Image 2026-03-25 at 23 57 17](https://github.com/user-attachments/assets/a3044fca-7921-42ad-a3c3-22afaeba6a25)
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

### 📝 License
Distributed under the MIT License. See LICENSE for more information.

# “The secret of getting ahead is getting started.” — Mark Twain


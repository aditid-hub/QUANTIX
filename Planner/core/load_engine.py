import os
import joblib
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Path inside your Drive folder
MODEL_DIR = "models"
MODEL_PATH = os.path.join(MODEL_DIR, "priority_model.pkl")

def train_and_save_model():
    """Trains a simple Decision Tree and saves it to the Drive 'models' folder."""
    # Dummy data: [Days_Left, Estimated_Hours]
    data = {
        'days_left': [1, 5, 2, 7, 3, 10],
        'hours_needed': [10, 2, 8, 1, 5, 1],
        'priority': [3, 1, 3, 1, 2, 1]  # 3: High, 2: Medium, 1: Low
    }
    df = pd.DataFrame(data)
    
    X = df[['days_left', 'hours_needed']]
    y = df['priority']
    
    model = DecisionTreeClassifier()
    model.fit(X, y)
    
    # Ensure the models directory exists in Drive
    os.makedirs(MODEL_DIR, exist_ok=True)
    
    # Save the model permanently
    joblib.dump(model, MODEL_PATH)
    return model

def get_model():
    """Loads the model from Drive; trains it if it doesn't exist."""
    if os.path.exists(MODEL_PATH):
        return joblib.load(MODEL_PATH)
    else:
        return train_and_save_model()

def predict_priority(days_left, hours_needed):
    """Predicts task priority using the Decision Tree."""
    model = get_model()
    prediction = model.predict([[days_left, hours_needed]])
    
    mapping = {3: "High", 2: "Medium", 1: "Low"}
    return mapping.get(prediction[0], "Medium")
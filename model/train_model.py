import sys
import os

# allow Python to find the app folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from app.feature_extractor import extract_features

# load dataset
data = pd.read_csv("data/phishing_dataset.csv")

urls = data["url"]
labels = data["label"]

# extract features
X = [extract_features(url) for url in urls]
y = labels

# split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# train model
model = RandomForestClassifier(n_estimators=200)
model.fit(X_train, y_train)

# save model
joblib.dump(model, "model/phishing_model.pkl")

print("Model trained and saved successfully!")

import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

from app.feature_extractor import extract_features

data = pd.read_csv("../data/phishing_dataset.csv")

urls = data["url"]
labels = data["label"]

X = [extract_features(url) for url in urls]

X_train, X_test, y_train, y_test = train_test_split(
    X, labels, test_size=0.2
)

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

joblib.dump(model, "phishing_model.pkl")

print("Model trained and saved.")
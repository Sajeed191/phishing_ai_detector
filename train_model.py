import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

data = pd.read_csv("phishing_dataset.csv")

X = data["email"]
y = data["label"]

vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(X).toarray()

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

model = Sequential()

model.add(Dense(32,input_dim=X.shape[1],activation="relu"))
model.add(Dense(16,activation="relu"))
model.add(Dense(1,activation="sigmoid"))

model.compile(
    loss="binary_crossentropy",
    optimizer="adam",
    metrics=["accuracy"]
)

model.fit(X_train,y_train,epochs=20)

model.save("phishing_model.h5")

import pickle
pickle.dump(vectorizer,open("vectorizer.pkl","wb"))

print("Model trained successfully")

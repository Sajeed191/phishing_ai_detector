from flask import Flask, render_template, request
import pickle
from tensorflow.keras.models import load_model

app = Flask(__name__)

model = load_model("phishing_model.h5")
vectorizer = pickle.load(open("vectorizer.pkl","rb"))

@app.route("/",methods=["GET","POST"])
def index():

    prediction = ""
    risk = ""

    if request.method=="POST":

        email = request.form["email"]

        data = vectorizer.transform([email]).toarray()

        result = model.predict(data)[0][0]

        if result > 0.5:
            prediction = "⚠ Phishing Email Detected"
            risk = "High Risk 🔴"
        else:
            prediction = "✅ Legitimate Email"
            risk = "Low Risk 🟢"

    return render_template("index.html",prediction=prediction,risk=risk)

if __name__ == "__main__":
    app.run(debug=True)

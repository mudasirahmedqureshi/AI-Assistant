from flask import Flask, render_template, request, jsonify
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-pro")

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json["message"]
    try:
        response = model.generate_content(user_msg)
        reply = response.text.strip()
    except Exception as e:
        reply = f"Error from Gemini: {e}"
    return jsonify({"reply": reply})

# Notice we no longer call app.run() here—Gunicorn will serve it.



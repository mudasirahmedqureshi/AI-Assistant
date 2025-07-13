from flask import Flask, render_template, request, jsonify
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Initialize Gemini
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
        reply = f"Error from Gemini: {str(e)}"

    return jsonify({"reply": reply})

if __name__ == "__main__":
    # For development only; use a production server for deployment
   app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))



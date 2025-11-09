import os
from flask import Flask, request, render_template, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Configure Gemini with your Railway environment variable
genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))

# Use Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/rewrite", methods=["POST"])
def rewrite():
    text = request.form["text"]
    response = model.generate_content(f"Rewrite this text in a natural, human-like way:\n{text}")
    return jsonify({"rewritten_text": response.text})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

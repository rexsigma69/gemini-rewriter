from flask import Flask, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

# Load your Gemini API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

@app.route("/rewrite", methods=["POST"])
def rewrite():
    data = request.get_json()
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(f"Rewrite this text to sound more natural and human:\n\n{text}")
        rewritten = response.text
        return jsonify({"rewritten": rewritten})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Gemini backend is running!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

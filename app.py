from flask import Flask, request, jsonify, render_template
from together import Together
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
client = Together()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate-image", methods=["POST"])
def generate_image():
    data = request.get_json()
    prompt = data.get("prompt")

    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    try:
        response = client.images.generate(
            prompt=prompt,
            model="black-forest-labs/FLUX.1-schnell",
            width=1024,
            height=768,
            steps=4,
            n=1,
            response_format="b64_json"
        )
        image_data = response.data[0].b64_json
        return jsonify({"image_data": image_data}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from caption_model import generate_caption

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET"])
def home():
    return "🟢 Flask server is running!"

@app.route("/caption", methods=["POST"])
def caption():
    print("🔵 [Flask] Received caption request")

    if "image" not in request.files:
        print("🔴 [Flask] No image found in request.files")
        return jsonify({"error": "No image uploaded"}), 400

    image = request.files["image"]
    if image.filename == "":
        print("🔴 [Flask] Empty filename")
        return jsonify({"error": "No selected file"}), 400

    try:
        image_path = os.path.join(UPLOAD_FOLDER, image.filename)
        print(f"🟡 [Flask] Saving image to {image_path}")
        image.save(image_path)

        print("🟢 [Flask] Generating caption...")
        caption = generate_caption(image_path)

        print("🟢 [Flask] Caption:", caption)
        return jsonify({"caption": caption})
    except Exception as e:
        print("🔴 [Flask] Error:", str(e))
        return jsonify({"error": "Internal server error", "message": str(e)}), 500
if __name__ == "__main__":
    app.run(debug=True)

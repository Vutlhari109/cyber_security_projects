from flask import Flask, request
import subprocess
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/run", methods=["POST"])
def run_uploaded_script():
    uploaded_file = request.files.get("file")
    address = request.args.get("address", "")
    port = request.args.get("port", "")
    domain = request.args.get("domain", "")

    if not uploaded_file:
        return "No file uploaded.", 400

    filepath = os.path.join(UPLOAD_FOLDER, uploaded_file.filename)
    uploaded_file.save(filepath)

    try:
        # Run the uploaded script with arguments
        result = subprocess.run(
            ["python3", filepath, address, port, domain],
            capture_output=True,
            text=True
        )
        return f"Output:\n{result.stdout}\nErrors:\n{result.stderr}"
    finally:
        os.remove(filepath)

if __name__ == "__main__":
    app.run(debug=True)
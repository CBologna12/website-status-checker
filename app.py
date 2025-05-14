from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def check_website(url):
    try:
        response = requests.get(url, timeout=5)
        return "Online" if response.status_code == 200 else f"Error {response.status_code}"
    except:
        return "Offline"

@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    if request.method == "POST":
        urls_text = request.form.get("urls", "")
        urls = [url.strip() for url in urls_text.splitlines() if url.strip()]
        for url in urls:
            status = check_website(url)
            results.append({"url": url, "status": status})
    return render_template("index.html", results=results)

if __name__ == "__main__":
    import os
port = int(os.environ.get("PORT", 5000))
app.run(debug=True, host="0.0.0.0", port=port)


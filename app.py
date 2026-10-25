from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
	return "Welcome to BookNest! Authentication is coming soon, with new books added every week."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
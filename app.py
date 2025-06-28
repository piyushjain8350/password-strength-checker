from flask import Flask, render_template, request
from password_checker import check_password_strength, generate_strong_password

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    strength = None
    password = ""
    suggested_password = None
    if request.method == "POST":
        if "password" in request.form:
            password = request.form["password"]
            strength = check_password_strength(password)
        elif "generate" in request.form:
            suggested_password = generate_strong_password()
    return render_template("index.html", strength=strength, password=password, suggested_password=suggested_password)

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        # Aquí puedes añadir validación (por ahora solo redirige)
        return redirect(url_for("index"))
    return render_template("login.html")

@app.route("/inicio")
def index():
    return render_template("index.html")

@app.route("/calendario")
def calendario():
    return render_template("calendario.html")

if __name__ == "__main__":
    app.run(debug=True)

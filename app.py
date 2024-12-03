from flask import Flask, render_template, request, redirect, url_for
ExceptionGroup = [404, 500]

app = Flask(__name__)

#main branch
@app.route("/")
def home():
    return render_template("index.html")

#login branch
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Get the form data
        email = request.form.get("email")
        password = request.form.get("password")
        
        # Dummy validation
        if email == "admin@example.com" and password == "password":
            return redirect(url_for("home"))
        else:
            return "Invalid credentials. Please try again."

    return render_template("login.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request, redirect
from user import User
app = Flask(__name__)

@app.route("/")
def index():
    users = User.get_all()
    print(users)
    return render_template("index.html", all_users = users)

@app.route('/add_user', methods=["POST"])
def add_user():
    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
    User.save(data)
    return redirect('/')

@app.route('/create')
def create():
    return render_template("/create.html")


if __name__ == "__main__":
    app.run(debug=True)
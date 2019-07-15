from flask import Flask, render_template, render_template, request

app = Flask(__name__)

# list used as a database here, could use sqlite3
db = []

@app.route("/")
def index():
    if not request.form:
        title = "Error on index page"
        message =" Please route to /register to fill the form in order to access the index page. thank you!!"
        return render_template("error.html", title=title, message=message)
    else:
        title = "Index page"
        return render_template("index.html", title=title)


@app.route("/register")
def register():
    title = "Form"
    return render_template("form.html", title=title)


@app.route("/validate", methods=["POST"])
def validate():
    
    name = request.form.get("name")
    course = request.form.get("course")
    number = request.form.get("number")

    if not name or not course or not number:
        title = "Registration Error"
        message ="Please route to /register, and add your name, course and number. thank you!!"
        return render_template("error.html", title=title, message=message)
    else:
        title = "Success Index-page"
        return render_template("index.html", title=title, name=name, course=course, number=number)

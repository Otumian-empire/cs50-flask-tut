from flask import Flask, render_template, request

# create a form-page
# validate the form and add the data to the db
# then route to registered-applicants
# or display error message to user on form-page

# using a list as db, this will be delete when he server is restarted
db = []

# initializing flask
app = Flask(__name__)

# default route/index-page
# is a form-page
# we take, first-name, last-name, index-number, faulty and activity
# from the user as input
@app.route("/")
def form_page():
    title = "Registration - Sports activity"
    message = ""
    return render_template("form.html", title=title, message=message)

# pass the data from the form page on submit to /validate
# to validate and then the data to the db (our list)
@app.route("/validate", methods=["POST"])
def validate_form():

    first_name = request.form.get("first-name")
    last_name = request.form.get("last-name")
    index_number = request.form.get("index-number")
    faculty = request.form.get("faculty")
    activity = request.form.get("activity")

    if not first_name or not last_name or not index_number or not faculty or not activity:
        title = "Registration - Sports activity"
        message = "All the fields are needed to have completed the form."
        return render_template("form.html", title=title, message=message)
    else:
        title= "REGISTERED APPLICANTS.."
        message = "You have registered successfully, look up your details.."
        row = []
        row.append(first_name)
        row.append(last_name)
        row.append(index_number)
        row.append(faculty)
        row.append(activity)
        db.append(row)

        return render_template("registered-applicants.html", title=title, message=message, db=db)

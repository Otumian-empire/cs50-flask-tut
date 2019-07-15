from flask import Flask, render_template, request
from csv import writer, reader

# create a form-page
# validate the form and add the data to a csv file
# then route to registered-applicants
# or display error message to user on form-page

# === we are now using a csv file to keep the records ===

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
        title= "Registration successful..."
        message = "You have registered successfully.."

        # writing data into the csv file
        with open("csv_db.csv", "a+") as f:
            # here enclose the data into a tuple or a list
            # there is writerows also
            writer(f).writerow([first_name, last_name, index_number, faculty, activity])
        

        return render_template("success.html", title=title, message=message, first_name=first_name)

@app.route("/registered-applicants")
def registered_applicants():
    
    title = "Registered Applicants"
    message = "Registered applicant list.."
    # reading data from the csv file
    with open("csv_db.csv", "r") as f:
        # here enclose the data into a tuple or a list
        # there is writerows also
        obj = list(reader(f))

        return render_template("registered-applicants.html", title=title, message=message, obj=obj)

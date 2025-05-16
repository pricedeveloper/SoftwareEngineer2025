"""
Paula Rice
Lab 14, Flask application
"""
from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask_sqlalchemy import SQLAlchemy

""" create an object 'app' from the Flask Module
 **name** set to __main__ if the script is running from the main file.
"""
app = Flask(__name__)
app.secret_key = "your_secret_key"

# connecting to Postgresql
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:11tommie@localhost/demoDB"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# create a DB object
db = SQLAlchemy(app)

# create a secret key to handle data within our server
import os
app.config["SECRET_KEY"] = os.urandom(24)

# define a model (create table in the "demoDB database")
class Userlogin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    userid = db.Column(db.Integer, nullable=False)


# define an employee model
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.String(20), unique=True, nullable=False)
    employee_name = db.Column(db.String(100), nullable=False)

# set the routing to the main page
# route decorator is used to access the root URL
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return "Successful Request! Entered password = " + request.form["password"]
    name = "price"
    checkfruit = "kiwi"
    fruits = ["apple", "grapes", "orange"]  # Example list of fruits
    return render_template("index.html", username=name, listfruits=fruits, checkfruit=checkfruit)

@app.route("/about")  # <== end points
def about():
    return render_template("about.html")

@app.route("/users", methods=["GET", "POST"])
def users():
    if request.method == "POST":
        try:
            form = request.form
            emp_name = form["employee_name"]
            emp_id = form["employee_id"]
            
            # Check if employee already exists by name (or use employee_id if that's unique)
            existing_employee = Employee.query.filter_by(employee_name=emp_name).first()
            existing_id = Employee.query.filter_by(employee_id=emp_id).first()
            
            if existing_employee:
                flash(f"Employee with name \"{emp_name}\" already exist!")
            if existing_id:
                flash(f"Employee with id \"{emp_id}\" already exist!")
            
            # Create new Employee object and add to database
            new_employee = Employee(employee_id=emp_id, employee_name=emp_name)
            
            # store first employee name in session
            session["employee1"] = new_employee.employee_name
            
            # add the new object to the database
            db.session.add(new_employee)
            db.session.commit()
            
            # message using flash
            flash(f"{request.form['employee_name']} Successfully Added!")
        except:
            flash("Fail to insert data! Try again")
    return render_template("users.html")

@app.route("/add_employee", methods=["POST"])
def add_employee():
    new_employee = [{"employee_name": "Alice"}]  # Example input
    session["employee1"] = new_employee[0]["employee_name"]
    return redirect(url_for("show_employee"))

@app.route("/show_employee")
def show_employee():
    return f"First employee: {session.get('employee1', 'Not set')}"

@app.route("/quotes")
def quotes():
    return redirect(url_for("index"))

# set the 'app' to run if you execute the file directly (not when it is imported)
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True)

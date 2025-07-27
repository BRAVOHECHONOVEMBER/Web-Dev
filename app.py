from flask import Flask, render_template, request, redirect, flash
import mysql.connector
from werkzeug.security 
import generate_password_hash

app = Flask(__name__)
app.secret_key = '06978ce38819fa8ca4c55125d4ce01a0' #generated with python

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="insert_your_password",
    database="flask_app"
)
cursor = db.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        print("Form submitted")
        print("Username:", username)
        print("Password:", password)

        # Hash the password before saving
        hashed_password = generate_password_hash(password)

        # Save to DB
        try:
            cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
            db.commit()
            flash("Signup successful!", "success")
        except Exception as e:
            db.rollback()
            flash(f"Error: {e}", "danger")

        return redirect('/signup')

    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)

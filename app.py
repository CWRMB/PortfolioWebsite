from flask import Flask, render_template, redirect, url_for, request
from forms import ContactForm
from flask import request
import pandas as pd

app = Flask(__name__)
app.secret_key = 'secretKey'


@app.route("/")
def home():
    title = "Michael Bennett's Portfolio"
    return render_template("index.html", title=title)


@app.route("/about")
def about():
    title = "About Me"
    return render_template("about.html", title=title)


@app.route('/contact', methods=["GET", "POST"])
def get_contact():
    form = ContactForm()
    # here, if the request type is a POST we get the data on contact
    # forms and save them else we return the contact forms html page
    if request.method == 'POST':
        name = request.form["name"]
        email = request.form["email"]
        subject = request.form["subject"]
        message = request.form["message"]
        res = pd.DataFrame({'name': name, 'email': email, 'subject': subject, 'message': message}, index=[0])
        res.to_csv('contactMessage.csv')
        print("Email / message request saved !")
    else:
        return render_template('form.html', form=form)
    return render_template('submissionSuccess.html')

if __name__ == '__main__':
    app.run()

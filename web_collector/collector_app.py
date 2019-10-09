from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import smtplib
from email.mime.text import  MIMEText
from sqlalchemy.sql import func

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://wc1:wc123@localhost/wc_1"
db = SQLAlchemy(app)


class Data(db.Model):
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key=True)
    email_ = db.Column(db.String(150), unique=True)
    salary_ = db.Column(db.Integer)

    def __init__(self, email, salary):
        self.email_ = email
        self.salary_ = salary


@app.route("/")
def main():
    return render_template("index.html")


@app.route("/thank_you_page_route", methods=['POST'])
def done():
    if request.method == "POST":
        input_email = request.form["input_email"]
        input_salary = request.form["input_salary"]
        if db.session.query(Data).filter(Data.email_ == input_email).count() == 0:
            data = Data(input_email, input_salary)
            db.session.add(data)
            db.session.commit()
            average_salary = db.session.query(func.avg(Data.salary_)).scalar()
            # send_email(input_email, input_salary, average_salary)
            return render_template("success.html")
        else:
            return render_template("index.html", text="Seems like you already have something from that email address")


def send_email(to_email, salary, average_salary):
    from_email = ""
    from_passwd = ""

    message = f"Hi,\nYour salary is {salary}. Average salary in you country is {average_salary}."
    msg = MIMEText(message, 'html')
    msg['Subject'] = "Salary statistic"
    msg['To'] = to_email
    msg['From'] = from_email

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_passwd)
    gmail.send_message(msg)


if __name__ == '__main__':
    app.debug = True
    app.run()

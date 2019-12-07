from flask import Flask

app = Flask(__name__)  # calls constructor for creating global Flask application object

"""
Decorator route is an attribute of app object initialized in line 3
This decorator says the main_view responds to "/" URL - localhost:5000/
"""
@app.route('/')
def main_view():
    # implementation of view (MVC - this is a controller)
    return "Hello World"


@app.route('/add1')  # additional_page_1 responds to localhost:5000/add1
def additional_page_1():
    return "Hello, this is an additional page :)"


if __name__ == "__main__":
    app.run()  # starting Flask app

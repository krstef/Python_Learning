from flask import Blueprint

simple_view = Blueprint('simple_view', __name__, template_folder='views')

@simple_view.route("/")
def main_view():
    return "Hi, new blueprint"

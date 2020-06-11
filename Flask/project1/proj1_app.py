from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def main_view():
    # render_template looks in the 'template' directory by default
    # welcome_text keyword is an example of passing values to html template using Jinja2
    return render_template("extended_index.html", welcome_text="This is simple bookmarking site. Developed for learning purposes.")


@app.route('/add')
def add_url():
    return render_template('add_url.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)  # run aplication in debug mode

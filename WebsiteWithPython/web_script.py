from flask import Flask, render_template
from pandas_datareader import data
import datetime
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.resources import CDN


app = Flask(__name__)


# you can change route here
# '/' means default route -> this route will be run when app starts
@app.route('/')
def home():
    return render_template("home.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/hashMe')
def graph():
    val = generate_chart()
    return render_template("graph.html",
                           javascript_placeholder=val[0],
                           html_placeholder=val[1],
                           # cdn_css_placeholder=cdn_css,
                           cdn_js_placeholder=val[2])


def generate_chart():
    start_time = datetime.datetime(2018, 7, 1)
    end_time = datetime.datetime(2018, 7, 12)

    data_frame = data.DataReader('GOOG', 'yahoo', start_time, end_time)

    data_frame["Status"] = [inc_dec(close, open_) for close, open_ in zip(data_frame.Close, data_frame.Open)]
    data_frame["Middle"] = (data_frame.Open + data_frame.Close) / 2

    plot = figure(x_axis_type='datetime', width=1000, height=300)

    plot.title.text = "Financial graph"
    plot.grid.grid_line_alpha = 0.3

    hours = 12 * 60 * 60 * 1000

    plot.rect(data_frame.index[data_frame.Status == "Increase"], (data_frame.Open + data_frame.Close) / 2, hours,
              abs(data_frame.Open - data_frame.Close), fill_color="green", line_color="black")

    plot.rect(data_frame.index[data_frame.Status == "Decrease"], (data_frame.Open + data_frame.Close) / 2, hours,
              abs(data_frame.Open - data_frame.Close), fill_color="red", line_color="black")

    javascript_part, html_part = components(plot)
    # TODO fix cdn_css, not visible in bokeh html
    # cdn_css = CDN.css_files[0]
    cdn_js = CDN.js_files[0]

    return javascript_part, html_part, cdn_js


def inc_dec(close, open_):
    if close > open_:
        return "Increase"
    elif close < open_:
        return "Decrease"
    else:
        return "Equal"

if __name__ == "__main__":
    app.run(debug=True)

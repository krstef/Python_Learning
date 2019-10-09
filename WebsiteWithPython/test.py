from pandas_datareader import data
import datetime
from bokeh.plotting import figure, output_file, show
from bokeh.embed import components
from bokeh.resources import CDN


def func():
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
              abs(data_frame.Open - data_frame.Close), fill_color="#7FFF00", line_color="black")

    plot.rect(data_frame.index[data_frame.Status == "Decrease"], (data_frame.Open + data_frame.Close) / 2, hours,
              abs(data_frame.Open - data_frame.Close), fill_color="red", line_color="black")

    javascript_part, html_part = components(plot)
    # TODO -> cdn_css is None object type, fix this
    # cdn_css = CDN.css_files[0]
    cdn_js = CDN.js_files[0]
    output_file("Lepo.html")
    show(plot)


def inc_dec(close, open_):
    if close > open_:
        return "Increase"
    elif close < open_:
        return "Decrease"
    else:
        return "Equal"


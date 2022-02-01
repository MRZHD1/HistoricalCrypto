import plotly.graph_objs as go
import csv
import numpy as np
from sympy import *
from sympy import poly


async def creategraph(cur1, cur2, day=None):
    # Open CSV file
    with open("currency.csv", "r") as f:
        csv_file = csv.reader(f)
        raw_array = []
        for i, line in enumerate(csv_file):
            if True:
                try:
                    raw_array.append([-i, float(line[1])])
                except:
                    pass
            next(csv_file)

        # Convert data into numpy array
        points = np.array(raw_array)

    # Initializing x
    x = Symbol('x')


    x_points = points[:, 0]
    y = points[:, 1]

    # Creates line of best fit and information regarding it
    z = np.polyfit(x_points, y, 15)
    f = np.poly1d(z)

    # Creates a list version of the numpy array containing function constants
    f_array = f.c
    c = f_array.tolist()

    # Creates a new reversed constants list
    coefficients = c[::-1]

    # Creates polynomial with and without h (very small value)
    y_func = poly(x ** 15 * c[0])
    y_hfunc = poly((x+0.00001) ** 15 * c[0])
    coefficients.pop()

    for i in range(15, 0, -1):
        if i > 1:
            g_func = poly(coefficients[i-1] * (x ** (i-1)))
            g_hfunc = poly(coefficients[i-1] * ((x+0.00001) ** (i-1)))
        else:
            g_func = coefficients[i-1]
            g_hfunc = coefficients[i-1]
        y_func += g_func
        y_hfunc += g_hfunc

    # Final derivative, using the limit definition (with small values of h)
    derivative = (y_hfunc - y_func)/0.00001

    x_new = np.linspace(x_points[0], x_points[-1], 50)
    y_new = f(x_new)

    # Creating the dataset, and generating the plot
    trace1 = go.Scatter(
        x=x_points,
        y=y,
        mode='markers',
        marker=go.scatter.Marker(color='rgb(255, 127, 14)'),
        name='Data'
    )

    # Creating the pattern, and generating the plot
    trace2 = go.Scatter(
        x=x_new,
        y=y_new,
        mode='lines',
        marker=go.scatter.Marker(color='rgb(31, 119, 180)'),
        name='Fit'
    )


    annotation = go.layout.Annotation(
        x=6,
        y=-4.5,
        text='',
        showarrow=False
    )

    # Designing presentation settings
    layout = go.Layout(
        title=f'{cur1} vs {cur2}',
        plot_bgcolor='rgb(229, 229, 229)',
        xaxis=go.layout.XAxis(zerolinecolor='rgb(255,255,255)', gridcolor='rgb(255,255,255)'),
        yaxis=go.layout.YAxis(zerolinecolor='rgb(255,255,255)', gridcolor='rgb(255,255,255)'),
        annotations=[annotation]
    )

    data = [trace1, trace2]

    # Drawing graph and exporting it
    fig = go.Figure(data=data, layout=layout)
    fig.write_image("fig1.png")
    if day is not None:
        print(raw_array[day])
        return derivative.subs(x, raw_array[day][0])

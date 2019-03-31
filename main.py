import io
import random
from flask import Flask, Response, request
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import json

app = Flask(__name__)

@app.route('/plot', methods=['POST'])
def plot_png():
    if request.method=='POST':
        js = request.json['data']
        print(request.json)
        fig = create_figure(js)
        output = io.BytesIO()
        FigureCanvas(fig).print_png(output)
        return Response(output.getvalue(), mimetype='image/png')

def create_figure(js):
    months = [js[i]["month"] for i in range(len(js))]
    expenses = [js[i]["expenses"] for i in range(len(js))]
    income = [js[i]["income"] for i in range(len(js))]
    savings = [js[i]["savings"] for i in range(len(js))]
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    xs = range(len(js))
    axis.plot(xs, expenses)
    axis.legend(['Expenses'])
    axis.plot(xs, income)
    axis.legend(['Income'])
    axis.plot(xs, savings)
    axis.legend(['Savings'])
    plt.xticks(xs, months)
    return fig

app.run(debug=True)

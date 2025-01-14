# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 18:05:10 2025

@author: Abhishek
"""

from flask import Flask, render_template, request
import pandas as pd
import plotly.express as px

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file:
        df = pd.read_csv(file)
        fig = px.bar(df, x="token", y="profit_percentage", color="token", title="Profit Percentage by Token")
        graph_html = fig.to_html(full_html=False)
        return render_template('results.html', table=df.to_html(classes='table table-bordered'), graph=graph_html)
    return "No file uploaded."

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request
import pandas as pd
import plotly.express as px

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file:
        df = pd.read_csv(file)
        fig = px.bar(df, x="token", y="profit_percentage", color="token", title="Profit Percentage by Token")
        graph_html = fig.to_html(full_html=False)
        return render_template('results.html', table=df.to_html(classes='table table-bordered'), graph=graph_html)
    return "No file uploaded."

if __name__ == "__main__":
    app.run(debug=True)

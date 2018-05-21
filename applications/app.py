from flask import Flask, render_template

import json
import plotly

import pandas as pd
import numpy as np
import plotly.graph_objs as go

app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
   
   # Read dataframe
    df =  pd.read_csv('actors_genre_rating.csv')

    graphs = [
        dict(
        data = [
            go.Bar(
            x=df['name'], # assign x as the dataframe column 'x'
            y=df['IMDB'],
            name = 'IMDB',
            marker=dict(
            color='rgb(0,0,255)',
            line=dict(
                color='rgb(8,48,107)',
                width=1.5)),
            opacity=0.6
        )],
        data=[
            go.Bar(
                x=df['name'],
                y=df['Metacritic'],
                name = 'Metacritic',
                marker=dict(
                color='rgb(0,255,0)',
            line=dict(
                color='rgb(8,48,107)',
                width=1.5)),
            opacity=0.6
    )],
        data=[
            go.Bar(
                x=df['name'],
                y=df['Rotten Tomatoes'],
                name = 'Rotten Tomatoes',
                marker=dict(
                color='rgb(255,0,0)',
                line=dict(
                    color='rgb(8,48,107)',
                    width=1.5)),
                opacity = 0.6
    )],
    
    layout = dict(
        title='Best Picture Winners Ratings',
    
        yaxis=dict(
            title='Ratings (%)',
            titlefont=dict(
            family='Courier New, monospace',
            size=14,
            color='black'
                          )
                  )
                  )
)  

    # Convert the figures to JSON
    graphJSON = json.dumps(graph, cls=plotly.utils.PlotlyJSONEncoder)

    # Render the Template
    return render_template('index.html', graphJSON=graphJSON)

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=9999)
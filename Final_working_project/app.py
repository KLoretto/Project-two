import os

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
app = Flask(__name__)


#################################################
# Database Setup
#################################################
from flask_sqlalchemy import SQLAlchemy
# The database URI
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db/oscar_winners_db.sqlite"

db = SQLAlchemy(app)

class Oscar(db.Model):
    __tablename__ = 'OSCAR_TABLE'

    id = db.Column(db.Integer, primary_key=True)
    film = db.Column(db.String)
    year = db.Column(db.String)
    ceremony = db.Column(db.Integer)
    award = db.Column(db.String)
    winner = db.Column(db.Integer)
    name = db.Column(db.String)
    budget = db.Column(db.Integer)
    revenue = db.Column(db.Integer)
    genre = db.Column(db.String)
    city = db.Column(db.String)
    lat = db.Column(db.Float)
    lon = db.Column(db.Float)
    imdb = db.Column(db.Integer)
    metacritic = db.Column(db.Integer)
    rottentomatoes = db.Column(db.Integer)


    def __repr__(self):
        return '<oscar %r>' % (self.name)


# Create database tables
@app.before_first_request
def setup():
    # Recreate database each time for demo
    # db.drop_all()
    db.create_all()

################################################
# Flask Routes
#################################################


@app.route("/")
def index():
    """Return the homepage."""
    return render_template('index.html')

@app.route("/dashboard")
def dashboard():
    """Return the homepage."""
    return render_template('dash.html')

@app.route("/table")
def table():
    """Return the homepage."""
    return render_template('table.html')

@app.route("/map")
def map():
    """Return the homepage."""
    return render_template('city-markers.html')


@app.route('/actor')
def actor():
    """Return a list of sample names."""

        # Use Pandas to perform the sql query
    stmt = db.session.query(Oscar.id, Oscar.film, Oscar.year, Oscar.genre, Oscar.name, Oscar.budget, Oscar.revenue, Oscar.ceremony, Oscar.winner, Oscar.imdb, Oscar.metacritic, Oscar.rottentomatoes,Oscar.award).\
                filter(Oscar.award == "Actor in a Leading Role").all()
    df = pd.DataFrame(stmt)
    # df_actor = df.filter[df['award'] == 'Actor in a Leading Role']

    actors = []
    for result in stmt:
        actors.append({

            "id": result[0],
            "film": result[1],
            "year": result[2],
            "genre": result[3],
            "name": result[4],
            "budget": result[5],
            "revenue": result[6],
            "ceremony": result[7],
            "winner": result[8],
            "imdb": result[9],
            "metacritic": result[10],
            "rottentomates": result[11],
            "award": result[12]

        })
    return jsonify(actors)


@app.route('/actress')
def actress():
    """Return a list of sample names."""

        # Use Pandas to perform the sql query
    stmt = db.session.query(Oscar.id, Oscar.film, Oscar.year, Oscar.genre, Oscar.name, Oscar.budget, Oscar.revenue, Oscar.ceremony, Oscar.winner, Oscar.imdb, Oscar.metacritic, Oscar.rottentomatoes,Oscar.award).\
                filter(Oscar.award == "Actress in a Leading Role").all()
    actors = []
    for result in stmt:
        actors.append({

            "id": result[0],
            "film": result[1],
            "year": result[2],
            "genre": result[3],
            "name": result[4],
            "budget": result[5],
            "revenue": result[6],
            "ceremony": result[7],
            "winner": result[8],
            "imdb": result[9],
            "metacritic": result[10],
            "rottentomates": result[11],
            "award": result[12]

        })
    return jsonify(actors)

@app.route('/Director')
def Director():
    """Return a list of sample names."""

        # Use Pandas to perform the sql query
    stmt = db.session.query(Oscar.id, Oscar.film, Oscar.year, Oscar.genre, Oscar.name, Oscar.budget, Oscar.revenue, Oscar.ceremony, Oscar.winner, Oscar.imdb, Oscar.metacritic, Oscar.rottentomatoes,Oscar.award).\
                filter(Oscar.award == "Directing").all()
    actors = []
    for result in stmt:
        actors.append({

            "id": result[0],
            "film": result[1],
            "year": result[2],
            "genre": result[3],
            "name": result[4],
            "budget": result[5],
            "revenue": result[6],
            "ceremony": result[7],
            "winner": result[8],
            "imdb": result[9],
            "metacritic": result[10],
            "rottentomates": result[11],
            "award": result[12]

        })
    return jsonify(actors)


@app.route('/Best_Picture')
def Best_Picture():
    """Return a list of sample names."""


        # Use Pandas to perform the sql query
    stmt = db.session.query(Oscar.id, Oscar.film, Oscar.year, Oscar.genre, Oscar.name, Oscar.budget, Oscar.revenue, Oscar.ceremony, Oscar.winner, Oscar.imdb, Oscar.metacritic, Oscar.rottentomatoes,Oscar.award).\
                filter(Oscar.award == "Best Picture").all()
    actors = []
    for result in stmt:
        actors.append({

            "id": result[0],
            "film": result[1],
            "year": result[2],
            "genre": result[3],
            "name": result[4],
            "budget": result[5],
            "revenue": result[6],
            "ceremony": result[7],
            "winner": result[8],
            "imdb": result[9],
            "metacritic": result[10],
            "rottentomates": result[11],
            "award": result[12]

        })
    return jsonify(actors)

@app.route('/actor_bar')
def actor_bar():
    """Return a list of sample names."""


        # Use Pandas to perform the sql query
    stmt = db.session.query(Oscar.id, Oscar.film, Oscar.year, Oscar.genre, Oscar.name, Oscar.budget, Oscar.revenue, Oscar.ceremony, Oscar.winner, Oscar.imdb, Oscar.metacritic, Oscar.rottentomatoes,Oscar.award).\
                filter(Oscar.award == "Actor in a Leading Role").all()

    film = [result[1] for result in stmt]
    metacritic = [result[10] for result in stmt]
    imdb = [result[9] for result in stmt]
    rottentomates = [result[11] for result in stmt]
    trace1 = {
        "x": film,
        "y": imdb,
        "name": "IMDB",
        "type": "bar"
    }
    trace2 = {
        "x": film,
        "y": rottentomates,
        "name": "rottentomatoes",
        "type": "bar"
    }
    trace3 = {
        "x": film,
        "y": metacritic,
        "name": "metacritic",
        "type": "bar"
    }
    # data = [trace1, trace2, trace3]

    data = [trace1, trace2, trace3]
    return jsonify(data)

@app.route('/actress_bar')
def actress_bar():
    """Return a list of sample names."""


        # Use Pandas to perform the sql query
    stmt = db.session.query(Oscar.id, Oscar.film, Oscar.year, Oscar.genre, Oscar.name, Oscar.budget, Oscar.revenue, Oscar.ceremony, Oscar.winner, Oscar.imdb, Oscar.metacritic, Oscar.rottentomatoes,Oscar.award).\
                filter(Oscar.award == "Actress in a Leading Role").all()

    film = [result[1] for result in stmt]
    metacritic = [result[10] for result in stmt]
    imdb = [result[9] for result in stmt]
    rottentomates = [result[11] for result in stmt]
    trace1 = {
        "x": film,
        "y": imdb,
        "name": "IMDB",
        "type": "bar"
    }
    trace2 = {
        "x": film,
        "y": rottentomates,
        "name": "rottentomatoes",
        "type": "bar"
    }
    trace3 = {
        "x": film,
        "y": metacritic,
        "name": "metacritic",
        "type": "bar"
    }
    # data = [trace1, trace2, trace3]

    data = [trace1, trace2, trace3]
    return jsonify(data)

@app.route('/director_bar')
def director_bar():
    """Return a list of sample names."""


        # Use Pandas to perform the sql query
    stmt = db.session.query(Oscar.id, Oscar.film, Oscar.year, Oscar.genre, Oscar.name, Oscar.budget, Oscar.revenue, Oscar.ceremony, Oscar.winner, Oscar.imdb, Oscar.metacritic, Oscar.rottentomatoes,Oscar.award).\
                filter(Oscar.award == "Directing").all()

    film = [result[1] for result in stmt]
    metacritic = [result[10] for result in stmt]
    imdb = [result[9] for result in stmt]
    rottentomates = [result[11] for result in stmt]
    trace1 = {
        "x": film,
        "y": imdb,
        "name": "IMDB",
        "type": "bar"
    }
    trace2 = {
        "x": film,
        "y": rottentomates,
        "name": "rottentomatoes",
        "type": "bar"
    }
    trace3 = {
        "x": film,
        "y": metacritic,
        "name": "metacritic",
        "type": "bar"
    }
    data = [trace1, trace2, trace3]

    return jsonify(data)

@app.route('/picture_bar')
def picture_bar():
    """Return a list of sample names."""


        # Use Pandas to perform the sql query
    stmt = db.session.query(Oscar.id, Oscar.film, Oscar.year, Oscar.genre, Oscar.name, Oscar.budget, Oscar.revenue, Oscar.ceremony, Oscar.winner, Oscar.imdb, Oscar.metacritic, Oscar.rottentomatoes,Oscar.award).\
                filter(Oscar.award == "Best Picture").all()

    film = [result[1] for result in stmt]
    metacritic = [result[10] for result in stmt]
    imdb = [result[9] for result in stmt]
    rottentomates = [result[11] for result in stmt]
    trace1 = {
        "x": film,
        "y": imdb,
         "name": "imdb",
        "type": "bar"
    }
    trace2 = {
        "x": film,
        "y": metacritic,
         "name": "metacritic",
        "type": "bar"
    }
    trace3 = {
        "x": film,
        "y": rottentomates,
        "name": "rottentomates",
        "type": "bar"
    }
    
    data = [trace1, trace2, trace3]
    return jsonify(data)
@app.route('/picture_scatter')
def picture_scatter():
    """Return a list of sample names."""


        # Use Pandas to perform the sql query
    stmt = db.session.query(Oscar.id, Oscar.film, Oscar.year, Oscar.genre, Oscar.name, Oscar.budget, Oscar.revenue, Oscar.ceremony, Oscar.winner, Oscar.imdb, Oscar.metacritic, Oscar.rottentomatoes,Oscar.award).\
                filter(Oscar.award == "Best Picture").all()

    budget = [result[5] for result in stmt]
    revenue = [result[6] for result in stmt]
    film = [result[1] for result in stmt]

    trace1 = {
        "x": budget,
        "y": revenue,
        "mode": 'markers',
        "type": 'scatter',
        "name": 'Films',
        "text": film,
        "textposition": 'top center',
        "textfont": {
            "family":  'Raleway, sans-serif'
    },

    }   

    return jsonify(trace1)

@app.route('/actor_scatter')
def actor_scatter():
    """Return a list of sample names."""


        # Use Pandas to perform the sql query
    stmt = db.session.query(Oscar.id, Oscar.film, Oscar.year, Oscar.genre, Oscar.name, Oscar.budget, Oscar.revenue, Oscar.ceremony, Oscar.winner, Oscar.imdb, Oscar.metacritic, Oscar.rottentomatoes,Oscar.award).\
                filter(Oscar.award == "Actor in a Leading Role").all()

    budget = [result[5] for result in stmt]
    revenue = [result[6] for result in stmt]
    film = [result[1] for result in stmt]

    trace1 = {
        "x": budget,
        "y": revenue,
        "mode": 'markers',
        "type": 'scatter',
        "name": 'Films',
        "text": film,
        "textposition": 'top center',
        "textfont": {
            "family":  'Raleway, sans-serif'
    },

    }   

    return jsonify(trace1)

@app.route('/actress_scatter')
def actress_scatter():
    """Return a list of sample names."""


        # Use Pandas to perform the sql query
    stmt = db.session.query(Oscar.id, Oscar.film, Oscar.year, Oscar.genre, Oscar.name, Oscar.budget, Oscar.revenue, Oscar.ceremony, Oscar.winner, Oscar.imdb, Oscar.metacritic, Oscar.rottentomatoes,Oscar.award).\
                filter(Oscar.award == "Actress in a Leading Role").all()

    budget = [result[5] for result in stmt]
    revenue = [result[6] for result in stmt]
    film = [result[1] for result in stmt]

    trace1 = {
        "x": budget,
        "y": revenue,
        "mode": 'markers',
        "type": 'scatter',
        "name": 'Films',
        "text": film,
        "textposition": 'top center',
        "textfont": {
            "family":  'Raleway, sans-serif'
    },

    }   

    return jsonify(trace1)

@app.route('/director_scatter')
def director_scatter():
    """Return a list of sample names."""


        # Use Pandas to perform the sql query
    stmt = db.session.query(Oscar.id, Oscar.film, Oscar.year, Oscar.genre, Oscar.name, Oscar.budget, Oscar.revenue, Oscar.ceremony, Oscar.winner, Oscar.imdb, Oscar.metacritic, Oscar.rottentomatoes,Oscar.award).\
                filter(Oscar.award == "Directing").all()

    budget = [result[5] for result in stmt]
    revenue = [result[6] for result in stmt]
    film = [result[1] for result in stmt]

    trace1 = {
        "x": budget,
        "y": revenue,
        "mode": 'markers',
        "type": 'scatter',
        "name": 'Films',
        "text": film,
        "textposition": 'top center',
    }   

    return jsonify(trace1)


@app.route('/actor_pie')
def actor_pie():
    """Return a list of sample names."""


    trace1 = {
            "values": [11, 9, 3, 2, 1, 0, 0, 0],
            "labels": ["Biography", "Drama", "Comedy", "Crime", "Action", "Adventure", "Sci-fi", "Western"],
            "colors": ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b", "#800080", "#C5B358", "#FF1493"],
            "hoverinfo":"label+percent", 
            "textinfo":"label",     
            "type": "pie"
    }
    return jsonify(trace1)

@app.route('/actress_pie')
def actress_pie():
    """Return a list of sample names."""   


    trace1 = {
            "values": [8, 11, 4, 3, 0, 0, 0, 0],
            "labels": ["Biography", "Drama", "Comedy", "Crime", "Action", "Adventure", "Sci-fi", "Western"],
            "colors": ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b", "#800080", "#C5B358", "#FF1493"],
            "hoverinfo":"label+percent", 
            "textinfo":"label",     
            "type": "pie"
    }
    return jsonify(trace1)

@app.route('/Director_pie')
def director_pie():
    """Return a list of sample names."""   


    trace1 = {
            "values": [5, 9, 3, 3, 1, 3, 1, 1],
            "labels": ["Biography", "Drama", "Comedy", "Crime", "Action", "Adventure", "Sci-fi", "Western"],
            "colors": ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b", "#800080", "#C5B358", "#FF1493"],
            "hoverinfo":"label+percent", 
            "textinfo":"label",     
            "type": "pie"
    }
    return jsonify(trace1)

@app.route('/Best_pie')
def best_pie():
    """Return a list of sample names."""   


    trace1 = {
            "values": [6, 9, 4, 3, 1, 2, 0, 1],
            "labels": ["Biography", "Drama", "Comedy", "Crime", "Action", "Adventure", "Sci-fi", "Western"],
            "colors": ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b", "#800080", "#C5B358", "#FF1493"],
            "hoverinfo":"label+percent", 
            "textinfo":"label",     
            "type": "pie"
    }
    return jsonify(trace1)



if __name__ == "__main__":
    app.run(debug=True)
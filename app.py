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

    # id = db.Column(db.Integer, primary_key=True)
    # emoji_char = db.Column(db.String)
    # emoji_id = db.Column(db.String)
    # name = db.Column(db.String)
    # score = db.Column(db.Integer)
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

# dbfile = os.path.join('db', 'oscar_winners_db.sqlite')
# engine = create_engine(f"sqlite:///{dbfile}")

# # reflect an existing database into a new model
# Base = automap_base()
# # reflect the tables
# Base.prepare(engine, reflect=True)

# # Save references to each table
# winner = Base.classes.OSCAR_TABLE
# test = Base.classes.sqlite_sequence
# # Create our session (link) from Python to the DB
# session = Session(engine)




# Create database tables
@app.before_first_request
def setup():
    # Recreate database each time for demo
    # db.drop_all()
    db.create_all()

################################################
# Flask Routes
#################################################


# @app.route("/")
# def index():
#     """Return the homepage."""
#     return render_template('index.html')


@app.route('/actor')
def actor():
    """Return a list of sample names."""

    # # Use Pandas to perform the sql query
    # results = db.session.query(Oscar.film, Oscar.award).\
    #     order_by(Oscar.film.desc()).\
    #     limit(10).all()
    # # Select the top 10 query results
    # film = [result[0] for result in results]
    # award = [result[1] for result in results]

    # # Generate the plot trace
    # plot_trace = {
    #     "x": film,
    #     "y": award,
    #     "type": "bar"
    # }
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

    # # Use Pandas to perform the sql query
    # results = db.session.query(Oscar.film, Oscar.award).\
    #     order_by(Oscar.film.desc()).\
    #     limit(10).all()
    # # Select the top 10 query results
    # film = [result[0] for result in results]
    # award = [result[1] for result in results]

    # # Generate the plot trace
    # plot_trace = {
    #     "x": film,
    #     "y": award,
    #     "type": "bar"
    # }
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

    # # Use Pandas to perform the sql query
    # results = db.session.query(Oscar.film, Oscar.award).\
    #     order_by(Oscar.film.desc()).\
    #     limit(10).all()
    # # Select the top 10 query results
    # film = [result[0] for result in results]
    # award = [result[1] for result in results]

    # # Generate the plot trace
    # plot_trace = {
    #     "x": film,
    #     "y": award,
    #     "type": "bar"
    # }
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

    # # Use Pandas to perform the sql query
    # results = db.session.query(Oscar.film, Oscar.award).\
    #     order_by(Oscar.film.desc()).\
    #     limit(10).all()
    # # Select the top 10 query results
    # film = [result[0] for result in results]
    # award = [result[1] for result in results]

    # # Generate the plot trace
    # plot_trace = {
    #     "x": film,
    #     "y": award,
    #     "type": "bar"
    # }
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


# @app.route('/best_picture')
# def actress():
#     """Return a list of sample names."""

#     # Use Pandas to perform the sql query
#     stmt = session.query(Oscars).statement
#     df = pd.read_sql_query(stmt, session.bind)
#     df_bp = df.loc[df['Award'] == 'Best Picture']

#     # Return a list of the column names (sample names)
#     return jsonify(df_bp)


if __name__ == "__main__":
    app.run(debug=True)
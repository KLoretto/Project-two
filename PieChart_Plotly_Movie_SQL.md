

```python
### Best Movie - Genre

import pandas as pd
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.graph_objs import Pie, Layout
import sqlite3 
from sqlalchemy import create_engine

### Will Need to Remove my key Info
plotly.tools.set_credentials_file(username='KL1234', api_key='3iyizDWmlaV1O65Zip4N')
### Will Need to Remove my key Info


#Will need to update path
engine = create_engine('sqlite:///oscar_winners_db.sqlite')
conn = engine.connect()


df_movie = pd.read_sql_query("select genre from oscars WHERE award='Best Picture'", conn)

# Verify that result of SQL query is stored in the dataframe
print(df_movie)

```

            Genre
    0   Adventure
    1       Drama
    2       Crime
    3      Comedy
    4   Biography
    5   Biography
    6      Comedy
    7   Biography
    8       Drama
    9       Drama
    10      Crime
    11      Crime
    12      Drama
    13      Drama
    14  Adventure
    15     Comedy
    16  Biography
    17     Action
    18      Drama
    19     Comedy
    20      Drama
    21      Drama
    22  Biography
    23      Drama
    24  Biography
    25    Western
    


```python

### Replace with SQLLite DB Info
genre_data_movie = df_movie["Genre"].value_counts()
genre_labels_movie = genre_data_movie.index.tolist()
genre_data_movie
```




    Drama        9
    Biography    6
    Comedy       4
    Crime        3
    Adventure    2
    Western      1
    Action       1
    Name: Genre, dtype: int64




```python
#Styled Plotly Pie Chart

colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b", "#800080", "#C5B358", "#FF1493"]


trace = go.Pie(labels=genre_labels_movie, values=genre_data_movie,
               hoverinfo='label+percent', textinfo='label',
               textfont=dict(size=17, color = '#FFFFFF'),
               marker=dict(colors=colors,
               line=dict(color='#000000', width=2)))

py.iplot([trace], filename='styled_pie_chart')
```




<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plot.ly/~KL1234/1.embed" height="525px" width="100%"></iframe>





```python
### Best Director - Genre

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


# Will need to update path
engine = create_engine('sqlite:///oscar_winners_db.sqlite')
conn = engine.connect()


df_director = pd.read_sql_query("select genre from oscars WHERE award='Directing'", conn)

# Verify that result of SQL query is stored in the dataframe
print(df_director)

```

            Genre
    0   Adventure
    1      Comedy
    2       Drama
    3      Comedy
    4      Sci-Fi
    5   Adventure
    6      Comedy
    7   Biography
    8       Drama
    9       Drama
    10      Crime
    11      Crime
    12      Drama
    13      Drama
    14  Adventure
    15  Biography
    16  Biography
    17      Crime
    18      Drama
    19     Action
    20      Drama
    21      Drama
    22  Biography
    23      Drama
    24  Biography
    25    Western
    


```python

### Replace with SQLLite DB Info
genre_data_director = df_director["Genre"].value_counts()
genre_labels_director = genre_data_director.index.tolist()
genre_data_director
```




    Drama        9
    Biography    5
    Adventure    3
    Crime        3
    Comedy       3
    Sci-Fi       1
    Western      1
    Action       1
    Name: Genre, dtype: int64




```python
#Styled Plotly Pie Chart

colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b", "#800080", "#C5B358", "#FF1493"]


trace = go.Pie(labels=genre_labels_director, values=genre_data_director,
               hoverinfo='label+percent', textinfo='label',
               textfont=dict(size=17, color = '#FFFFFF'),
               marker=dict(colors=colors,
               line=dict(color='#000000', width=2)))

py.iplot([trace], filename='styled_pie_chart')
```




<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plot.ly/~KL1234/1.embed" height="525px" width="100%"></iframe>



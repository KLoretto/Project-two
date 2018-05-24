

```python
### Best Actress - Genre

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


df_actress = pd.read_sql_query("select genre from oscars WHERE award='Actress in a Leading Role'", conn)

# Verify that result of SQL query is stored in the dataframe
print(df_actress)

```

            Genre
    0       Crime
    1      Comedy
    2       Drama
    3       Drama
    4       Drama
    5      Comedy
    6   Biography
    7       Drama
    8   Biography
    9       Drama
    10  Biography
    11  Biography
    12  Biography
    13      Drama
    14  Biography
    15      Drama
    16      Drama
    17  Biography
    18  Biography
    19     Comedy
    20     Comedy
    21      Crime
    22      Crime
    23      Drama
    24      Drama
    25      Drama
    


```python

### Replace with SQLLite DB Info
genre_data_actress = df_actress["Genre"].value_counts()
genre_labels_actress = genre_data_actress.index.tolist()
genre_data_actress
```




    Drama        11
    Biography     8
    Comedy        4
    Crime         3
    Name: Genre, dtype: int64




```python
#Styled Plotly Pie Chart

colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b", "#800080", "#C5B358", "#FF1493"]


trace = go.Pie(labels=genre_labels_actress, values=genre_data_actress,
               hoverinfo='label+percent', textinfo='label',
               textfont=dict(size=18, color = '#FFFFFF'),
               marker=dict(colors=colors,
               line=dict(color='#000000', width=2)))

py.iplot([trace], filename='styled_pie_chart')
```




<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plot.ly/~KL1234/1.embed" height="525px" width="100%"></iframe>



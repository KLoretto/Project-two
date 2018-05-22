

```python
### Best Actor - Genre

import pandas as pd
import matplotlib.pyplot as plt
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.graph_objs import Pie, Layout

### Will Need to Remove my key Info
plotly.tools.set_credentials_file(username='KL1234', api_key='3iyizDWmlaV1O65Zip4N')
### Will Need to Remove my key Info

### Will need to be updated with SQLLite DB Info
df =  pd.read_csv('actors_genre.csv')
genre_data_actor = df["genre1"].value_counts()
genre_labels_actor = genre_data_actor.index.tolist()
genre_data_actor
```




    Biography    10
    Drama         4
    Comedy        3
    Crime         2
    Action        1
    Adventure     1
    Name: genre1, dtype: int64




```python
#Styled Plotly Pie Chart

colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b", "#800080"]


trace = go.Pie(labels=genre_labels_actor, values=genre_data_actor,
               hoverinfo='label+percent', textinfo='label',
               textfont=dict(size=18, color = '#FFFFFF'),
               marker=dict(colors=colors,
               line=dict(color='#000000', width=2)))

py.iplot([trace], filename='styled_pie_chart')
```




<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plot.ly/~KL1234/1.embed" height="525px" width="100%"></iframe>



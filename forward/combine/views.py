from django.shortcuts import render
from django.http import HttpResponse
from forward.settings import MEDIA_URL,MEDIA_ROOT
from django.conf.urls.static import static
from django.views.generic import TemplateView, View 

# IMPORTS AND PLOT THE GRAPHS
import plotly.graph_objects as go
from plotly.subplots import make_subplots

df_commperday_price['Date'] = df_commperday_price['Date'].astype(str)
x_date = df_commperday_price['Date'].tolist()

y_commperday_price = df_commperday_price['Price'].tolist()
y_commperday_count = df_commperday_price['comm_count'].tolist()



# Create figure with secondary y-axis
fig = make_subplots(specs=[[{"secondary_y": True}]])

# Add traces
fig.add_trace(
    go.Scatter(x=x_date, y=y_commperday_count, name="Comments/day"),
    secondary_y=False,
)

fig.add_trace(
    go.Scatter(x=x_date, y=y_commperday_price, name="Price"),
    secondary_y=True,
)

# Add figure title
fig.update_layout(
    title_text="TopGlove Daily Number of Comments vs Price for 2 years"
)

# Set x-axis title
fig.update_xaxes(title_text="Month")

# Set y-axes titles
# fig.update_yaxes(title_text="<b>primary</b> yaxis title", secondary_y=False)
# fig.update_yaxes(title_text="<b>secondary</b> yaxis title", secondary_y=True)
fig.update_yaxes(title_text="Comments/day", secondary_y=False)
fig.update_yaxes(title_text="Price", secondary_y=True)

fig.show()
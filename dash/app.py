import dash
from dash import html

app = dash.Dash(__name__)
server = app.server

app.layout = html.Div(children=[
    html.H1(children="Hello World.")
])

if __name__ == "__main__":
    app.run_server(debug=True)

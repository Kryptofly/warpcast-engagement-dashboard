import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
from analysis.data_fetching import fetch_user_interactions
from analysis.data_analysis import analyze_engagement

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Warpcast User Engagement Dashboard"),
    dcc.Input(id='username-input', type='text', placeholder='Enter Warpcast username'),
    html.Button(id='submit-button', n_clicks=0, children='Submit'),
    dcc.Graph(id='engagement-graph'),
    dcc.Graph(id='engagement-timeline')
])

@app.callback(
    [Output('engagement-graph', 'figure'),
     Output('engagement-timeline', 'figure')],
    [Input('submit-button', 'n_clicks')],
    [dash.dependencies.State('username-input', 'value')]
)
def update_output(n_clicks, username):
    if n_clicks > 0 and username:
        interactions = fetch_user_interactions(username)
        engagement_summary, engagement_timeline = analyze_engagement(interactions)
        
        engagement_fig = {
            'data': [
                {'x': list(engagement_summary.keys()), 'y': list(engagement_summary.values()), 'type': 'bar'}
            ],
            'layout': {
                'title': 'User Engagement Summary'
            }
        }
        
        timeline_fig = {
            'data': [
                {'x': engagement_timeline['date'], 'y': engagement_timeline['likes'], 'type': 'line', 'name': 'Likes'},
                {'x': engagement_timeline['date'], 'y': engagement_timeline['comments'], 'type': 'line', 'name': 'Comments'},
                {'x': engagement_timeline['date'], 'y': engagement_timeline['recasts'], 'type': 'line', 'name': 'Recasts'}
            ],
            'layout': {
                'title': 'Engagement Over Time'
            }
        }
        
        return engagement_fig, timeline_fig
    return {}, {}

if __name__ == '__main__':
    app.run_server(debug=True)

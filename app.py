import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# print("Libraries imported!")

# Load data
df = pd.read_csv('global_house_purchase_dataset.csv')
# print(f"Data loaded! Shape: {df.shape}")

# Initialize app
app = dash.Dash(__name__)
server = app.server 

# Styles
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "250px",
    "padding": "35px 25px",
    "background": "linear-gradient(180deg, #1e3c72 0%, #2a5298 100%)",
    "boxShadow": "4px 0 15px rgba(0,0,0,0.15)",
    "zIndex": "1000"
}

CONTENT_STYLE = {
    "marginLeft": "270px",
    "marginRight": "20px",
    "padding": "40px",
    "backgroundColor": "#f5f6fa",
    "minHeight": "100vh"
}

# Define chart components
chart1_dashboard = dcc.Graph(id='chart1-dashboard', config={'displayModeBar': False})
chart2_dashboard = dcc.Graph(id='chart2-dashboard', config={'displayModeBar': False})
chart3_dashboard = dcc.Graph(id='chart3-dashboard', config={'displayModeBar': False})
chart4_dashboard = dcc.Graph(id='chart4-dashboard', config={'displayModeBar': False})
chart5_dashboard = dcc.Graph(id='chart5-dashboard', config={'displayModeBar': False})

metric_dropdown_dashboard = dcc.Dropdown(
    id='metric-dropdown-dashboard',
    options=[
        {'label': 'Loan Amount', 'value': 'loan_amount'},
        {'label': 'Down Payment', 'value': 'down_payment'}
    ],
    value='loan_amount',
    style={'marginBottom': '20px', 'fontSize': '14px'}
)

# Country-wise components
country_dropdown_main = dcc.Dropdown(
    id='country-dropdown-main',
    options=[{'label': c, 'value': c} for c in sorted(df['country'].unique())],
    value='USA',
    placeholder='Select a country...',
    style={'width': '300px', 'fontSize': '14px'}
)

city_dropdown_country = dcc.Dropdown(id='city-dropdown-country', options=[], placeholder='Select a city...', style={'marginBottom': '20px', 'fontSize': '14px'})
furnishing_dropdown_country = dcc.Dropdown(id='furnishing-dropdown-country', options=[], placeholder='Select furnishing...', style={'marginBottom': '20px', 'fontSize': '14px'})
financial_metric_dropdown_country = dcc.Dropdown(
    id='financial-metric-dropdown-country',
    options=[
        {'label': 'Avg Salary', 'value': 'customer_salary'},
        {'label': 'Avg Down Payment', 'value': 'down_payment'},
        {'label': 'Avg Loan Amount', 'value': 'loan_amount'}
    ],
    value='customer_salary',
    style={'marginBottom': '20px', 'fontSize': '14px'}
)
rooms_dropdown_country = dcc.Dropdown(id='rooms-dropdown-country', options=[], placeholder='Select rooms...', style={'marginBottom': '20px', 'fontSize': '14px'})
connectivity_dropdown_country = dcc.Dropdown(id='connectivity-dropdown-country', options=[], placeholder='Select connectivity...', style={'marginBottom': '20px', 'fontSize': '14px'})

chart1_country = dcc.Graph(id='chart1-country', config={'displayModeBar': False})
chart2_country = dcc.Graph(id='chart2-country', config={'displayModeBar': False})
chart3_country = dcc.Graph(id='chart3-country', config={'displayModeBar': False})
chart4_country = dcc.Graph(id='chart4-country', config={'displayModeBar': False})
chart5_country = dcc.Graph(id='chart5-country', config={'displayModeBar': False})

# Sidebar
sidebar = html.Div([
    html.Div([
        html.H2("Global House Purchase Dashboard", style={"color": "#fff", "fontSize": "30px", "fontWeight": "800", "marginBottom": "5px", "letterSpacing": "0.5px"}),
        html.P("Analytics Dashboard", style={"color": "rgba(255,255,255,0.75)", "fontSize": "14px", "marginBottom": "50px", "fontWeight": "300"})
    ]),
    
    dcc.Link(
    html.Div([
        html.Div("📊", style={"fontSize": "18px", "marginBottom": "4px"}),  # smaller icon
        html.Div("Dashboard", style={"fontSize": "14px", "fontWeight": "600"})  # smaller text
    ], style={"textAlign": "center"}),
    href="/",
    style={
        "display": "block",
        "padding": "8px 12px",   # reduced padding
        "color": "#fff",
        "textDecoration": "none",
        "borderRadius": "8px",   # smaller radius
        "marginBottom": "8px",   # less spacing below
        "background": "rgba(255,255,255,0.15)",
        "transition": "all 0.3s ease",
        "border": "1px solid rgba(255,255,255,0.2)"  # thinner border
    }
),
    
    dcc.Link(
        html.Div([
            html.Div("🌍", style={"fontSize": "18px", "marginBottom": "4px"}),
            html.Div("Country Analysis", style={"fontSize": "14px", "fontWeight": "600"})
        ], style={"textAlign": "center"}),
        href="/country-wise",
        style={
            "display": "block",
        "padding": "8px 12px",   # reduced padding
        "color": "#fff",
        "textDecoration": "none",
        "borderRadius": "8px",   # smaller radius
        "marginBottom": "8px",   # less spacing below
        "background": "rgba(255,255,255,0.15)",
        "transition": "all 0.3s ease",
        "border": "1px solid rgba(255,255,255,0.2)"  # thinner border
        }
    )
], style=SIDEBAR_STYLE)

# Dashboard Layout
dashboard_layout = html.Div([
    html.Div([
        html.H1("Global Comparision", 
                style={'color': '#1e3c72', 'fontSize': '38px', 'fontWeight': '800', 'marginBottom': '10px', 'letterSpacing': '-0.5px'}),
        html.P("Comprehensive market overview and insights", 
               style={'color': '#6c757d', 'fontSize': '15px', 'marginBottom': '0'})
    ], style={'marginBottom': '40px'}),
    
    # Top Chart
    html.Div([
        html.Div([
            html.H3("Country-wise Average Per Sqft Value", 
                    style={'color': '#2c3e50', 'marginBottom': '20px', 'fontSize': '20px', 'fontWeight': '700'}),
            chart1_dashboard
        ], style={
            'background': '#fff',
            'padding': '30px',
            'borderRadius': '15px',
            'boxShadow': '0 4px 15px rgba(0,0,0,0.08)',
            'border': '1px solid #e3e6eb'
        })
    ], style={'marginBottom': '30px'}),

    # 2x2 Grid
    html.Div([
        html.Div([
            html.Div([
                html.H3("Property Type Distribution", 
                        style={'color': '#2c3e50', 'marginBottom': '20px', 'fontSize': '18px', 'fontWeight': '700'}),
                chart2_dashboard
            ], style={
                'background': '#fff',
                'padding': '30px',
                'borderRadius': '15px',
                'boxShadow': '0 4px 15px rgba(0,0,0,0.08)',
                'border': '1px solid #e3e6eb',
                'height': '550px'
            })
        ], style={'width': '49%', 'display': 'inline-block', 'verticalAlign': 'top'}),

        html.Div([
            html.Div([
                html.H3("Financial Comparison", 
                        style={'color': '#2c3e50', 'marginBottom': '15px', 'fontSize': '18px', 'fontWeight': '700'}),
                metric_dropdown_dashboard,
                chart3_dashboard
            ], style={
                'background': '#fff',
                'padding': '30px',
                'borderRadius': '15px',
                'boxShadow': '0 4px 15px rgba(0,0,0,0.08)',
                'border': '1px solid #e3e6eb',
                'height': '550px'
            })
        ], style={'width': '49%', 'display': 'inline-block', 'verticalAlign': 'top', 'marginLeft': '2%'}),
    ], style={'marginBottom': '30px'}),

    html.Div([
        html.Div([
            html.Div([
                html.H3("Salary Distribution", 
                        style={'color': '#2c3e50', 'marginBottom': '20px', 'fontSize': '18px', 'fontWeight': '700'}),
                chart4_dashboard
            ], style={
                'background': '#fff',
                'padding': '30px',
                'borderRadius': '15px',
                'boxShadow': '0 4px 15px rgba(0,0,0,0.08)',
                'border': '1px solid #e3e6eb',
                'height': '550px'
            })
        ], style={'width': '49%', 'display': 'inline-block', 'verticalAlign': 'top'}),

        html.Div([
            html.Div([
                html.H3("Salary vs Loan Comparison", 
                        style={'color': '#2c3e50', 'marginBottom': '20px', 'fontSize': '18px', 'fontWeight': '700'}),
                chart5_dashboard
            ], style={
                'background': '#fff',
                'padding': '30px',
                'borderRadius': '15px',
                'boxShadow': '0 4px 15px rgba(0,0,0,0.08)',
                'border': '1px solid #e3e6eb',
                'height': '550px'
            })
        ], style={'width': '49%', 'display': 'inline-block', 'verticalAlign': 'top', 'marginLeft': '2%'}),
    ])
])

# Country-wise Layout
countrywise_layout = html.Div([
    html.Div([
        html.H1("Country-wise Market Analysis", 
                style={'color': '#1e3c72', 'fontSize': '38px', 'fontWeight': '800', 'marginBottom': '10px', 'letterSpacing': '-0.5px'}),
        html.P("Detailed insights by location and filters", 
               style={'color': '#6c757d', 'fontSize': '15px', 'marginBottom': '0'})
    ], style={'marginBottom': '35px'}),
    
    html.Div([
        html.Label("Country:", style={'fontWeight': '700', 'fontSize': '15px', 'marginRight': '15px', 'color': '#2c3e50'}),
        country_dropdown_main
    ], style={'marginBottom': '40px', 'background': 'white', 'padding': '25px 30px', 'borderRadius': '12px', 
              'boxShadow': '0 4px 15px rgba(0,0,0,0.08)', 'display': 'inline-block', 'border': '1px solid #e3e6eb'}),
    
    # Row 1 - Single Large Chart
    html.Div([
        html.Div([
            html.H3("Average Property Price by Type", style={'color': '#2c3e50', 'fontSize': '20px', 'fontWeight': '700', 'marginBottom': '20px'}),
            city_dropdown_country,
            chart1_country
        ], style={'background': 'white', 'padding': '35px', 'borderRadius': '15px', 'boxShadow': '0 4px 15px rgba(0,0,0,0.08)', 'height': '650px', 'border': '1px solid #e3e6eb'})
    ], style={'marginBottom': '35px'}),
    
    # Row 2 - Two Charts Side by Side
    html.Div([
        html.Div([
            html.Div([
                html.H3("Property Type Analysis", style={'color': '#2c3e50', 'fontSize': '19px', 'fontWeight': '700', 'marginBottom': '20px'}),
                furnishing_dropdown_country,
                chart2_country
            ], style={'background': 'white', 'padding': '35px', 'borderRadius': '15px', 'boxShadow': '0 4px 15px rgba(0,0,0,0.08)', 'height': '700px', 'border': '1px solid #e3e6eb'})
        ], style={'width': '49%', 'display': 'inline-block', 'verticalAlign': 'top'}),
        
        html.Div([
            html.Div([
                html.H3("Financial Requirements", style={'color': '#2c3e50', 'fontSize': '19px', 'fontWeight': '700', 'marginBottom': '20px'}),
                financial_metric_dropdown_country,
                chart3_country
            ], style={'background': 'white', 'padding': '35px', 'borderRadius': '15px', 'boxShadow': '0 4px 15px rgba(0,0,0,0.08)', 'height': '700px', 'border': '1px solid #e3e6eb'})
        ], style={'width': '49%', 'display': 'inline-block', 'verticalAlign': 'top', 'marginLeft': '2%'}),
    ], style={'marginBottom': '35px'}),
    
    # Row 3 - Two Charts Side by Side
    html.Div([
        html.Div([
            html.Div([
                html.H3("Price by Room Count", style={'color': '#2c3e50', 'fontSize': '19px', 'fontWeight': '700', 'marginBottom': '20px'}),
                rooms_dropdown_country,
                chart4_country
            ], style={'background': 'white', 'padding': '35px', 'borderRadius': '15px', 'boxShadow': '0 4px 15px rgba(0,0,0,0.08)', 'height': '650px', 'border': '1px solid #e3e6eb'})
        ], style={'width': '49%', 'display': 'inline-block', 'verticalAlign': 'top'}),
        
        html.Div([
            html.Div([
                html.H3("Price by Connectivity", style={'color': '#2c3e50', 'fontSize': '19px', 'fontWeight': '700', 'marginBottom': '20px'}),
                connectivity_dropdown_country,
                chart5_country
            ], style={'background': 'white', 'padding': '35px', 'borderRadius': '15px', 'boxShadow': '0 4px 15px rgba(0,0,0,0.08)', 'height': '650px', 'border': '1px solid #e3e6eb'})
        ], style={'width': '49%', 'display': 'inline-block', 'verticalAlign': 'top', 'marginLeft': '2%'}),
    ])
])

content = html.Div([dcc.Location(id='url', refresh=False), html.Div(id='page-content')], style=CONTENT_STYLE)

app.layout = html.Div([
    sidebar, content,
    html.Div([
        chart1_dashboard, chart2_dashboard, chart3_dashboard, chart4_dashboard, chart5_dashboard,
        metric_dropdown_dashboard, country_dropdown_main, city_dropdown_country, 
        furnishing_dropdown_country, financial_metric_dropdown_country, 
        rooms_dropdown_country, connectivity_dropdown_country,
        chart1_country, chart2_country, chart3_country, chart4_country, chart5_country
    ], style={'display': 'none'})
], style={'fontFamily': '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif'})

# Callbacks
@app.callback(Output('page-content', 'children'), Input('url', 'pathname'))
def display_page(pathname):
    return countrywise_layout if pathname == '/country-wise' else dashboard_layout

@app.callback(Output('chart1-dashboard', 'figure'), Input('chart1-dashboard', 'id'))
def update_dashboard_chart1(_):
    df['price_per_sqft'] = df['price'] / df['property_size_sqft']
    country_data = df.groupby('country')['price_per_sqft'].mean().reset_index()
    fig = px.choropleth(country_data, locations='country', locationmode='country names',
                        color='price_per_sqft', hover_name='country',
                        color_continuous_scale='Blues',
                        labels={'price_per_sqft': 'Price per Sqft ($)'})
    fig.update_layout(height=420, margin=dict(l=5, r=5, t=5, b=5),
                      geo=dict(showframe=False, showcoastlines=True, projection_type='natural earth'))
    return fig

@app.callback(Output('chart2-dashboard', 'figure'), Input('chart2-dashboard', 'id'))
def update_dashboard_chart2(_):
    heatmap_data = df.groupby(['country', 'property_type']).size().reset_index(name='count')
    heatmap_pivot = heatmap_data.pivot(index='country', columns='property_type', values='count').fillna(0)
    fig = px.imshow(heatmap_pivot, x=heatmap_pivot.columns, y=heatmap_pivot.index,
                    color_continuous_scale='Blues', aspect="auto",
                    labels=dict(x="Property Type", y="Country", color="Count"))
    fig.update_layout(height=470, margin=dict(l=5, r=5, t=5, b=5))
    fig.update_xaxes(tickangle=-45)
    return fig

@app.callback(Output('chart3-dashboard', 'figure'), Input('metric-dropdown-dashboard', 'value'))
def update_dashboard_chart3(metric):
    data = df.groupby('country')[metric].mean().reset_index().sort_values(metric, ascending=False)
    fig = px.bar(data, x='country', y=metric, color=metric, color_continuous_scale='Viridis')
    fig.update_layout(height=450, margin=dict(l=5, r=5, t=5, b=5), showlegend=False)
    fig.update_xaxes(tickangle=-45)
    return fig

@app.callback(Output('chart4-dashboard', 'figure'), Input('chart4-dashboard', 'id'))
def update_dashboard_chart4(_):
    fig = px.box(df, x='country', y='customer_salary', color='country')
    fig.update_layout(height=470, margin=dict(l=5, r=5, t=5, b=5), showlegend=False)
    fig.update_xaxes(tickangle=-45)
    return fig

@app.callback(Output('chart5-dashboard', 'figure'), Input('chart5-dashboard', 'id'))
def update_dashboard_chart5(_):
    data = df.groupby('country').agg({'customer_salary': 'mean', 'loan_amount': 'mean'}).reset_index()
    fig = go.Figure()
    fig.add_trace(go.Bar(x=data['country'], y=data['customer_salary'], name='Avg Salary', marker_color='#3498db'))
    fig.add_trace(go.Bar(x=data['country'], y=data['loan_amount'], name='Avg Loan', marker_color='#e74c3c'))
    fig.update_layout(height=470, margin=dict(l=5, r=5, t=5, b=5), barmode='group',
                      legend=dict(orientation="h", yanchor="top", y=1.1, xanchor="center", x=0.5))
    fig.update_xaxes(tickangle=-45)
    return fig

@app.callback(Output('city-dropdown-country', 'options'), Output('city-dropdown-country', 'value'), Input('country-dropdown-main', 'value'))
def populate_cities(country):
    if not country: return [], None
    cities = sorted(df[df['country'] == country]['city'].unique())
    return [{'label': c, 'value': c} for c in cities], cities[0] if cities else None

@app.callback(Output('chart1-country', 'figure'), Input('country-dropdown-main', 'value'), Input('city-dropdown-country', 'value'))
def update_country_chart1(country, city):
    if not country or not city: return px.bar().update_layout(height=530)
    filtered = df[(df['country'] == country) & (df['city'] == city)]
    if filtered.empty: return px.bar().update_layout(height=530)
    data = filtered.groupby('property_type')['price'].mean().reset_index().sort_values('price', ascending=False)
    fig = px.bar(data, x='property_type', y='price', color='property_type',
                 labels={'price': 'Average Price ($)', 'property_type': 'Property Type'})
    fig.update_layout(height=530, margin=dict(l=5, r=5, t=5, b=5), showlegend=False)
    fig.update_xaxes(tickangle=-45)
    return fig

@app.callback(Output('furnishing-dropdown-country', 'options'), Output('furnishing-dropdown-country', 'value'),
              Input('country-dropdown-main', 'value'), Input('city-dropdown-country', 'value'))
def populate_furnishing(country, city):
    if not country or not city: return [], None
    filtered = df[(df['country'] == country) & (df['city'] == city)]
    furn = sorted(filtered['furnishing_status'].unique())
    return [{'label': f, 'value': f} for f in furn], furn[0] if furn else None

@app.callback(Output('chart2-country', 'figure'), Input('country-dropdown-main', 'value'), 
              Input('city-dropdown-country', 'value'), Input('furnishing-dropdown-country', 'value'))
def update_country_chart2(country, city, furnishing):
    if not all([country, city, furnishing]): return px.scatter().update_layout(height=600)
    filtered = df[(df['country'] == country) & (df['city'] == city) & (df['furnishing_status'] == furnishing)]
    if filtered.empty: return px.scatter().update_layout(height=600)
    data = filtered.groupby('property_type').agg({'price': 'mean', 'property_size_sqft': 'mean'}).reset_index()
    fig = px.scatter(data, x='property_size_sqft', y='price', size='price', color='property_type', 
                     text='property_type', size_max=70,
                     labels={'price': 'Avg Price ($)', 'property_size_sqft': 'Size (sqft)', 'property_type': 'Type'})
    fig.update_traces(textposition='top center')
    fig.update_layout(height=600, margin=dict(l=5, r=5, t=60, b=5),
                      legend=dict(orientation="h", yanchor="top", y=1.12, xanchor="center", x=0.5))
    return fig

@app.callback(Output('chart3-country', 'figure'), Input('country-dropdown-main', 'value'), 
              Input('city-dropdown-country', 'value'), Input('furnishing-dropdown-country', 'value'),
              Input('financial-metric-dropdown-country', 'value'))
def update_country_chart3(country, city, furnishing, metric):
    if not all([country, city, furnishing]): return px.bar().update_layout(height=600)
    filtered = df[(df['country'] == country) & (df['city'] == city) & (df['furnishing_status'] == furnishing)]
    if filtered.empty: return px.bar().update_layout(height=600)
    data = filtered.groupby('property_type')[metric].mean().reset_index().sort_values(metric, ascending=False)
    fig = px.bar(data, x='property_type', y=metric, color='property_type',
                 labels={metric: 'Amount ($)', 'property_type': 'Type'})
    fig.update_layout(height=600, margin=dict(l=5, r=5, t=60, b=5),
                      legend=dict(orientation="h", yanchor="top", y=1.12, xanchor="center", x=0.5))
    fig.update_xaxes(tickangle=-45)
    return fig

@app.callback(Output('rooms-dropdown-country', 'options'), Output('rooms-dropdown-country', 'value'),
              Input('country-dropdown-main', 'value'), Input('city-dropdown-country', 'value'),
              Input('furnishing-dropdown-country', 'value'))
def populate_rooms(country, city, furnishing):
    if not all([country, city, furnishing]): return [], None
    filtered = df[(df['country'] == country) & (df['city'] == city) & (df['furnishing_status'] == furnishing)]
    rooms = sorted(filtered['rooms'].unique())
    return [{'label': f'{r} Rooms', 'value': r} for r in rooms], rooms[0] if rooms else None

@app.callback(Output('chart4-country', 'figure'), Input('country-dropdown-main', 'value'),
              Input('city-dropdown-country', 'value'), Input('furnishing-dropdown-country', 'value'),
              Input('rooms-dropdown-country', 'value'))
def update_country_chart4(country, city, furnishing, rooms):
    if not all([country, city, furnishing, rooms]): 
        return px.pie(title='Select all filters').update_layout(height=530)
    filtered = df[(df['country'] == country) & (df['city'] == city) & 
                  (df['furnishing_status'] == furnishing) & (df['rooms'] == rooms)]
    if filtered.empty: 
        return px.pie(title='No data available').update_layout(height=530)
    data = filtered.groupby('property_type')['price'].mean().reset_index().sort_values('price', ascending=False)
    fig = px.pie(data, values='price', names='property_type', 
                 title=f'Price Distribution by Property Type<br>{rooms} Rooms in {city}',
                 labels={'property_type': 'Property Type', 'price': 'Avg Price'},
                 hole=0.4,  # Makes it a donut chart
                 color_discrete_sequence=px.colors.qualitative.Set3)
    fig.update_traces(
        textposition='inside',
        textinfo='percent+label',
        hovertemplate='<b>%{label}</b><br>Avg Price: $%{value:,.0f}<br>Percentage: %{percent}<extra></extra>',
        pull=[0.05 if i == 0 else 0 for i in range(len(data))]  # Pull out the largest slice
    )
    fig.update_layout(
        height=530, 
        margin=dict(l=5, r=5, t=60, b=5),
        showlegend=True,
        legend=dict(
            orientation="v",
            yanchor="middle",
            y=0.5,
            xanchor="left",
            x=1.05
        )
    )
    return fig

@app.callback(Output('connectivity-dropdown-country', 'options'), Output('connectivity-dropdown-country', 'value'),
              Input('country-dropdown-main', 'value'), Input('city-dropdown-country', 'value'))
def populate_connectivity(country, city):
    if not country or not city: return [], None
    filtered = df[(df['country'] == country) & (df['city'] == city)]
    conn = sorted(filtered['connectivity_score'].unique())
    return [{'label': f'Score {c}', 'value': c} for c in conn], conn[0] if conn else None

@app.callback(Output('chart5-country', 'figure'), Input('country-dropdown-main', 'value'),
              Input('city-dropdown-country', 'value'), Input('connectivity-dropdown-country', 'value'))
def update_country_chart5(country, city, connectivity):
    if not all([country, city, connectivity]): 
        return px.pie(title='Select all filters').update_layout(height=530)
    filtered = df[(df['country'] == country) & (df['city'] == city) & (df['connectivity_score'] == connectivity)]
    if filtered.empty: 
        return px.pie(title='No data available').update_layout(height=530)
    data = filtered.groupby('property_type')['price'].mean().reset_index().sort_values('price', ascending=False)
    fig = px.pie(data, values='price', names='property_type',
                 title=f'Price Distribution by Property Type<br>Connectivity Score: {connectivity} in {city}',
                 labels={'property_type': 'Property Type', 'price': 'Avg Price'},
                 hole=0.4,  # Makes it a donut chart
                 color_discrete_sequence=px.colors.qualitative.Pastel)
    fig.update_traces(
        textposition='inside',
        textinfo='percent+label',
        hovertemplate='<b>%{label}</b><br>Avg Price: $%{value:,.0f}<br>Percentage: %{percent}<extra></extra>',
        pull=[0.05 if i == 0 else 0 for i in range(len(data))]  # Pull out the largest slice
    )
    fig.update_layout(
        height=530, 
        margin=dict(l=5, r=5, t=60, b=5),
        showlegend=True,
        legend=dict(
            orientation="v",
            yanchor="middle",
            y=0.5,
            xanchor="left",
            x=1.05
        )
    )
    return fig

if __name__ == '__main__':
    app.run_server(debug=False, host='0.0.0.0', port=8050)
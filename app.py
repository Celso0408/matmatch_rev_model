from dash import Dash, dcc, html
import plotly.graph_objects as go
from dash.dependencies import Input, Output


app = Dash(__name__)
server = app.server

fig = go.Figure()

quarters = ['Q1-2024', 'Q2-2024', 'Q3-2024', 'Q4-2024', 'Q1-2025', 'Q2-2025', 'Q3-2025', 'Q4-2025', 'Q1-2026', 'Q2-2026', 'Q3-2026', 'Q4-2026', 'Q1-2027', 'Q2-2027', 'Q3-2027', 'Q4-2027']

def calculate_total_revenue(values, weight, weight_percent):
    current_weight = weight * weight_percent
    return [value * current_weight for value in values]

cpc_relative_values = [0,0,1,2,5,10,20,50,100,175,225,250,256,262,269,275]
weight_cpc_percent = 1
weight_cpc = 2.5 * weight_cpc_percent
y_cpc = calculate_total_revenue(cpc_relative_values, weight_cpc, weight_cpc_percent)

fig.add_trace(go.Scatter(
    x = quarters,
    y = y_cpc,
    line=dict(color='orange'),
    marker=dict(symbol='square'),
    name='CpC'
))

donations_relative_values = [0,0,0,2,5,10,20,50,100,200,300,400,500,512,524,537,550]
weight_donations_percent = 1
weight_donations = 0.05 * weight_donations_percent
y_donations = calculate_total_revenue(donations_relative_values, weight_donations, weight_donations_percent)

fig.add_trace(go.Scatter(
    x = quarters,
    y = y_donations,
    line=dict(color='purple'),
    marker=dict(symbol='diamond'),
    name='Donations'
))

subscriptions_relative_values = [0,0,0,50,100,200,300,400,500,500,500,500,512,524,537,550] 
weight_subscriptions_percent = 1
weight_subscriptions = 0.1 * weight_subscriptions_percent
y_subscriptions = calculate_total_revenue(subscriptions_relative_values, weight_subscriptions, weight_subscriptions_percent)

fig.add_trace(go.Scatter(
    x = quarters,
    y = y_subscriptions,
    line=dict(color='gray'),
    marker=dict(symbol='triangle-up'),
    name='Subscriptions'
))

consulting_relative_values = [0,0,0,0,1,1,2,2,5,5,10,10,10,10,11,11]
weight_consulting_percent = 1
weight_consulting = 10 * weight_consulting_percent
y_consulting = calculate_total_revenue(consulting_relative_values, weight_consulting, weight_consulting_percent)

fig.add_trace(go.Scatter(
    x = quarters,
    y = y_consulting,
    line=dict(color='yellow'),
    marker=dict(symbol='x'),
    name='Consulting'
))

partnerships_relative_values = [0,0,0,0,0,1,2,5,10,12,14,16,16,17,17,18]
weight_partnerships_percent = 1
weight_partnerships = 10 * weight_partnerships_percent
y_partnerships = calculate_total_revenue(partnerships_relative_values, weight_partnerships, weight_partnerships_percent)

fig.add_trace(go.Scatter(
    x = quarters,
    y = y_partnerships,
    line=dict(color='blue'),
    marker=dict(symbol='x'),
    name='Partnerships'
))

transactions_relative_values = [0,0,0,0,0,0,1,2,5,10,20,30,31,31,32,33]
weight_transactions_percent = 1
weight_transactions = 5 * weight_transactions_percent
y_transactions = calculate_total_revenue(transactions_relative_values, weight_transactions, weight_transactions_percent)

fig.add_trace(go.Scatter(
    x = quarters,
    y = y_transactions,
    line=dict(color='green'),
    marker=dict(symbol='circle'),
    name='Transactions fee'
))

fig.update_xaxes(fixedrange=True)
fig.update_yaxes(
    tickvals=[0,100,200,300,400,500,600,700], 
    ticktext = [f"{i} k€" for i in range(0, 800, 100)],
    fixedrange=True
)
fig.update_layout(
    title=dict(
        text='Revenue Models',
        xanchor='center',
        x=0.5,
        font=dict(size=20)
    ),
    legend=dict(
        orientation='h',
        yanchor='bottom',
        y=1.02,
        xanchor='center',
        x=0.5,
        traceorder='normal',
        font=dict(size=10),
    )
)


""" TOTAL REVENUE GRAPH """

fig2 = go.Figure()

y_sum = [a + b + c + d + e + f for a, b, c, d, e, f in zip(y_cpc, y_donations, y_subscriptions, y_consulting, y_partnerships, y_transactions)]

fig2.add_trace(go.Scatter(
    x = quarters,
    y = y_sum,
    line=dict(color='blue'),
    marker=dict(symbol='circle'),
    name='Total Revenue'
))

fig2.update_xaxes(fixedrange=True)
fig2.update_yaxes(
    tickvals=[0,100,200,300,400,500,600,700, 800, 900, 1000, 1100, 1200, 1300, 1400], 
    ticktext = [f"{i} k€" for i in range(0, 1500, 100)],
    fixedrange=True
)

fig2.update_layout(
    title=dict(
        text='Total Revenue',
        xanchor='center',
        x=0.5,
        font=dict(size=20)
    )
)

""" PIZZA GRAPH 2024 """

sum_cpc_2024 = sum(y_cpc[:4])
sum_donations_2024 = sum(y_donations[:4])
sum_subscriptions_2024 = sum(y_subscriptions[:4])
sum_consulting_2024 = sum(y_consulting[:4])
sum_partnerships_2024 = sum(y_partnerships[:4])
sum_transactions_2024 = sum(y_transactions[:4])

sums = [sum_cpc_2024, sum_donations_2024, sum_subscriptions_2024, sum_consulting_2024, sum_partnerships_2024, sum_transactions_2024]
labels = ['CpC', 'Donations', 'Subscriptions', 'Consulting', 'Partnerships', 'Transactions']

values = [value for value in sums if value > 0]
labels = [label for label, value in zip(labels, sums) if value > 0]

colors = ['orange', 'gray', 'purple', 'gray', 'yellow', 'blue', 'green']

fig3 = go.Figure(data=[go.Pie(labels=labels, values=values, marker=dict(colors=colors))])

fig3.update_layout(
    title=dict(
        text='2024',
        xanchor='center',
        x=0.5,
        y=0.9,
        font=dict(size=20)
    ),
    legend=dict(
        orientation='h',
        yanchor='bottom',
        y=-0.2,
        xanchor='center',
        x=0.5,
        traceorder='normal',
        font=dict(size=10),
    )
)


""" PIZZA GRAPH 2025 """

sum_cpc_2025 = sum(y_cpc[4:8])
sum_donations_2025 = sum(y_donations[4:8])
sum_subscriptions_2025 = sum(y_subscriptions[4:8])
sum_consulting_2025 = sum(y_consulting[4:8])
sum_partnerships_2025 = sum(y_partnerships[4:8])
sum_transactions_2025 = sum(y_transactions[4:8])

sums = [sum_cpc_2025, sum_donations_2025, sum_subscriptions_2025, sum_consulting_2025, sum_partnerships_2025, sum_transactions_2025]
labels = ['CpC', 'Donations', 'Subscriptions', 'Consulting', 'Partnerships', 'Transactions']

values = [value for value in sums if value > 0]
labels = [label for label, value in zip(labels, sums) if value > 0]

colors = ['orange', 'purple', 'gray', 'yellow', 'blue', 'green']

fig4 = go.Figure(data=[go.Pie(labels=labels, values=values, marker=dict(colors=colors))])

fig4.update_layout(
    title=dict(
        text='2025',
        xanchor='center',
        x=0.5,
        y=0.875,
        font=dict(size=20)
    ),
    legend=dict(
        orientation='h',
        yanchor='bottom',
        y=-0.25,
        xanchor='center',
        x=0.5,
        traceorder='normal',
        font=dict(size=10),
    )
)


""" PIZZA GRAPH 2026 """

sum_cpc_2026 = sum(y_cpc[8:12])
sum_donations_2026 = sum(y_donations[8:12])
sum_subscriptions_2026 = sum(y_subscriptions[8:12])
sum_consulting_2026 = sum(y_consulting[8:12])
sum_partnerships_2026 = sum(y_partnerships[8:12])
sum_transactions_2026 = sum(y_transactions[8:12])

sums = [sum_cpc_2026, sum_donations_2026, sum_subscriptions_2026, sum_consulting_2026, sum_partnerships_2026, sum_transactions_2026]
labels = ['CpC', 'Donations', 'Subscriptions', 'Consulting', 'Partnerships', 'Transactions']

values = [value for value in sums if value > 0]
labels = [label for label, value in zip(labels, sums) if value > 0]

fig5 = go.Figure(data=[go.Pie(labels=labels, values=values, marker=dict(colors=colors))])

fig5.update_layout(
    title=dict(
        text='2026',
        xanchor='center',
        x=0.5,
        y=0.875,
        font=dict(size=20)
    ),
    legend=dict(
        orientation='h',
        yanchor='bottom',
        y=-0.25,
        xanchor='center',
        x=0.5,
        traceorder='normal',
        font=dict(size=10),
    )
)

""" PIZZA GRAPH 2027 """

sum_cpc_2027 = sum(y_cpc[12:16])
sum_donations_2027 = sum(y_donations[12:16])
sum_subscriptions_2027 = sum(y_subscriptions[12:16])
sum_consulting_2027 = sum(y_consulting[12:16])
sum_partnerships_2027 = sum(y_partnerships[12:16])
sum_transactions_2027 = sum(y_transactions[12:16])

sums = [sum_cpc_2027, sum_donations_2027, sum_subscriptions_2027, sum_consulting_2027, sum_partnerships_2027, sum_transactions_2027]
labels = ['CpC', 'Donations', 'Subscriptions', 'Consulting', 'Partnerships', 'Transactions']

values = [value for value in sums if value > 0]
labels = [label for label, value in zip(labels, sums) if value > 0]

colors = ['orange', 'purple', 'gray', 'yellow', 'blue', 'green']

fig6 = go.Figure(data=[go.Pie(labels=labels, values=values, marker=dict(colors=colors))])

fig6.update_layout(
    title=dict(
        text='2027',
        xanchor='center',
        x=0.5,
        y=0.875,
        font=dict(size=20)
    ),
    legend=dict(
        orientation='h',
        yanchor='bottom',
        y=-0.25,
        xanchor='center',
        x=0.5,
        traceorder='normal',
        font=dict(size=10),
    )
)

app.layout = html.Div([
    html.Div([
        dcc.Graph(
            id='graph1',
            figure=fig,
            style={'width': '40%', 'height': '100%'}
        ),
        html.Div([
            html.Label('CpC', style={'margin-left': '22px'}),
            dcc.Slider(
                id='slider-cpc',
                min=0,
                max=1,
                step=0.1,
                value=1
            ),
            html.Label('Donations', style={'margin-left': '22px'}),
            dcc.Slider(
                id='slider-donations',
                min=0,
                max=1,
                step=0.1,
                value=1
            ),
            html.Label('Subscriptions', style={'margin-left': '22px'}),
            dcc.Slider(
                id='slider-subscriptions',
                min=0,
                max=1,
                step=0.1,
                value=1
            ),
            html.Label('Consulting', style={'margin-left': '22px'}),
            dcc.Slider(
                id='slider-consulting',
                min=0,
                max=1,
                step=0.1,
                value=1
            ),
            html.Label('Partnerships', style={'margin-left': '22px'}),
            dcc.Slider(
                id='slider-partnerships',
                min=0,
                max=1,
                step=0.1,
                value=1
            ),
            html.Label('Transactions fee', style={'margin-left': '22px'}),
            dcc.Slider(
                id='slider-transactions',
                min=0,
                max=1,
                step=0.1,
                value=1
            ),
        ], style={'width': '15%', 'height': '100%', 'font-size': '12px', 'padding': '15px'}),
        dcc.Graph(
            id='graph2',
            figure=fig2,
            style={'width': '40%', 'height': '100%'}
        ),
    ], style={'width': '100%', 'height': '50%', 'display': 'flex', 'flex-direction': 'row', 'align-items': 'center'}),
    html.Div([
        dcc.Graph(
            id='graph3',
            figure=fig3,
            style={'width': '25%', 'display': 'inline-block'}
        ),
        dcc.Graph(
            id='graph4',
            figure=fig4,
            style={'width': '25%', 'display': 'inline-block'}
        ),
        dcc.Graph(
            id='graph5',
            figure=fig5,
            style={'width': '25%', 'display' : 'inline-block'}
        ),
        dcc.Graph(
            id='graph6',
            figure=fig6,
            style={'width': '25%', 'display' : 'inline-block'}
        ),
    ]),
], style={'height': '100%', 'width': '100%', 'align-items': 'center'})

def update_pie_chart(fig, y_values, start, end):
    sums = [sum(y[start:end]) for y in y_values]
    labels = ['CpC', 'Donations', 'Subscriptions', 'Consulting', 'Partnerships', 'Transactions']

    values = [value for value in sums if value > 0]
    labels = [label for label, value in zip(labels, sums) if value > 0]

    color_dict = {'CpC': 'orange', 'Donations': 'purple', 'Subscriptions': 'gray', 'Consulting': 'yellow', 'Partnerships': 'blue', 'Transactions': 'green'}
    colors = [color_dict[label] for label in labels]

    fig.data[0].labels = labels
    fig.data[0].values = values
    fig.data[0].marker.colors = colors

@app.callback(
    [Output('graph1', 'figure'),
     Output('graph2', 'figure'),
     Output('graph3', 'figure'),
     Output('graph4', 'figure'),
     Output('graph5', 'figure'),
     Output('graph6', 'figure')],
    [Input('slider-cpc', 'value'),
     Input('slider-donations', 'value'),
     Input('slider-subscriptions', 'value'),
     Input('slider-consulting', 'value'),
     Input('slider-partnerships', 'value'),
     Input('slider-transactions', 'value')]
)
def update_graphs(value_cpc, value_donations, value_subscriptions, value_consulting, value_partnerships, value_transactions):
    y_cpc = calculate_total_revenue(cpc_relative_values, weight_cpc, value_cpc)
    fig.update_traces(y=y_cpc, selector=dict(name='CpC'))
    fig3.update_traces(y=y_cpc, selector=dict(name='CpC'))
    fig4.update_traces(y=y_cpc, selector=dict(name='CpC'))
    fig5.update_traces(y=y_cpc, selector=dict(name='CpC'))
    fig6.update_traces(y=y_cpc, selector=dict(name='CpC'))

    y_donations = calculate_total_revenue(donations_relative_values, weight_donations, value_donations)
    fig.update_traces(y=y_donations, selector=dict(name='Donations'))
    fig3.update_traces(y=y_donations, selector=dict(name='Donations'))
    fig4.update_traces(y=y_donations, selector=dict(name='Donations'))
    fig5.update_traces(y=y_donations, selector=dict(name='Donations'))
    fig6.update_traces(y=y_donations, selector=dict(name='Donations'))

    y_subscriptions = calculate_total_revenue(subscriptions_relative_values, weight_subscriptions, value_subscriptions)
    fig.update_traces(y=y_subscriptions, selector=dict(name='Subscriptions'))
    fig3.update_traces(y=y_subscriptions, selector=dict(name='Subscriptions'))
    fig4.update_traces(y=y_subscriptions, selector=dict(name='Subscriptions'))
    fig5.update_traces(y=y_subscriptions, selector=dict(name='Subscriptions'))
    fig6.update_traces(y=y_subscriptions, selector=dict(name='Subscriptions'))

    y_consulting = calculate_total_revenue(consulting_relative_values, weight_consulting, value_consulting)
    fig.update_traces(y=y_consulting, selector=dict(name='Consulting'))
    fig3.update_traces(y=y_consulting, selector=dict(name='Consulting'))
    fig4.update_traces(y=y_consulting, selector=dict(name='Consulting'))
    fig5.update_traces(y=y_consulting, selector=dict(name='Consulting'))
    fig6.update_traces(y=y_consulting, selector=dict(name='Consulting'))

    y_partnerships = calculate_total_revenue(partnerships_relative_values, weight_partnerships, value_partnerships)
    fig.update_traces(y=y_partnerships, selector=dict(name='Partnerships'))
    fig3.update_traces(y=y_partnerships, selector=dict(name='Partnerships'))
    fig4.update_traces(y=y_partnerships, selector=dict(name='Partnerships'))
    fig5.update_traces(y=y_partnerships, selector=dict(name='Partnerships'))
    fig6.update_traces(y=y_partnerships, selector=dict(name='Partnerships'))

    y_transactions = calculate_total_revenue(transactions_relative_values, weight_transactions, value_transactions)
    fig.update_traces(y=y_transactions, selector=dict(name='Transactions fee'))
    fig3.update_traces(y=y_transactions, selector=dict(name='Transactions fee'))
    fig4.update_traces(y=y_transactions, selector=dict(name='Transactions fee'))
    fig5.update_traces(y=y_transactions, selector=dict(name='Transactions fee'))
    fig6.update_traces(y=y_transactions, selector=dict(name='Transactions fee'))

    y_sum = [a + b + c + d + e + f for a, b, c, d, e, f in zip(y_cpc, y_donations, y_subscriptions, y_consulting, y_partnerships, y_transactions)]
    fig2.update_traces(y=y_sum, selector=dict(name='Total Revenue'))

    """ UPDATE PIZZA GRAPH 2024 """

    y_values = [y_cpc, y_donations, y_subscriptions, y_consulting, y_partnerships, y_transactions]
    update_pie_chart(fig3, y_values, 0, 4)
    update_pie_chart(fig4, y_values, 4, 8) 
    update_pie_chart(fig5, y_values, 8, 12) 
    update_pie_chart(fig6, y_values, 12, 16) 

    return fig, fig2, fig3, fig4, fig5, fig6

if __name__ == '__main__':
    app.run_server(debug=True)

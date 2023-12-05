import shimoku_api_python as Shimoku
import datetime as dt

#----- Client initialization with playground mode -----#

s = Shimoku.Client(
    async_execution=True,  
    verbosity='INFO',      
)

s.set_workspace() 

s.set_board('Custom Board')

s.set_menu_path('catalog', 'Charts-example')

 

# ----------------------- Title: Bar chart ----------------------#
s.plt.html(
    order=0,
    html=s.html_components.panel(
        href='https://docs.shimoku.com/development/charts/charts/bar-charts',
        text='Bar Chart',
        button_panel='Read more',
        symbol_name='insights'
    )
)


language_expressiveness = [
    {'Language': 'C', 'Statements ratio': 1.0, 'Lines ratio': 1.0},
    {'Language': 'C++', 'Statements ratio': 2.5, 'Lines ratio': 1.0},
    {'Language': 'Fortran', 'Statements ratio': 2.0, 'Lines ratio': 0.8},
    {'Language': 'Java', 'Statements ratio': 2.5, 'Lines ratio': 1.5},
    {'Language': 'Perl', 'Statements ratio': 6.0, 'Lines ratio': 6.0},
    {'Language': 'Smalltalk', 'Statements ratio': 6.0, 'Lines ratio': 6.25},
    {'Language': 'Python', 'Statements ratio': 6.0, 'Lines ratio': 6.5},
    ]


s.plt.bar(
    order=1, title='Language expressiveness',
    data=language_expressiveness, x='Language',
    y=['Statements ratio', 'Lines ratio'],
)



# ----------------------- Title: Pie chart ----------------------#
s.plt.html(
    order=2,
    html=s.html_components.panel(
        href='https://docs.shimoku.com/development/charts/charts/pie-charts',
        text='Pie Chart',
        button_panel='Read more',
        symbol_name='insights'
    )
)

data_language = [
    {'Language': 'C', 'value': 78},
    {'Language': 'C++', 'value': 17},
    {'Language': 'Fortran', 'value': 18},
    {'Language': 'Java', 'value': 9},
]

s.plt.pie(
    data=data_language,
    names='Language',
    values='value',
    order = 3,
    rows_size=2,
    cols_size=12,
    title='LE pie'
    )



# ----------------------- Title: Gauge chart ----------------------#
s.plt.html(
    order=4,
    html=s.html_components.panel(
        href='https://docs.shimoku.com/development/charts/charts/gauge-charts',
        text='Gauge Chart',
        button_panel='Read more',
        symbol_name='insights'
    )
)

s.plt.shimoku_gauge(
    value=-48, order=5,
    rows_size=1, cols_size=3, name="Shimoku",
    color=1
)
    
s.plt.shimoku_gauge(
    value=3.56, order=6,
    rows_size=1, cols_size=3,
    color="status-error"
)
    
s.plt.shimoku_gauge(
    value=-90, order=7,
    rows_size=1, cols_size=3, name="gauges",
    color='#00F0FF'
)



# ------------------ Title: Line and Bar chart -----------------#
s.plt.html(
    order=8,
    html=s.html_components.panel(
        href='https://docs.shimoku.com/development/charts/charts/line-and-bar',
        text='Line and Bar Chart',
        button_panel='Read more',
        symbol_name='insights'
    )
)


data = [
    {'day': 'Mon', 'Evaporation': 2.0, 'Precipitation': 2.6, 'Temperature': 2.0},
    {'day': 'Tue', 'Evaporation': 4.9, 'Precipitation': 5.9, 'Temperature': 2.2},
    {'day': 'Wed', 'Evaporation': 7.0, 'Precipitation': 9.0, 'Temperature': 3.3},
    {'day': 'Thu', 'Evaporation': 23.2, 'Precipitation': 26.4, 'Temperature': 4.5},
    {'day': 'Fri', 'Evaporation': 25.6, 'Precipitation': 28.7, 'Temperature': 6.3},
    {'day': 'Sat', 'Evaporation': 76.7, 'Precipitation': 70.7, 'Temperature': 10.2},
    {'day': 'Sun', 'Evaporation': 135.6, 'Precipitation': 175.6, 'Temperature': 20.3}
]


s.plt.line_and_bar_charts(
    data=data, order=9, x='day', 
    bar_names=['Evaporation', 'Precipitation'], 
    line_names=['Temperature'],
    title='rainfall and temperature', 
    x_axis_name='Day', 
    line_axis_name='Temperature',
    line_suffix=' °C', 
    bar_axis_name='Evaporation and precipitacion', 
    bar_suffix=' ml'
)



# --------------------- Title: Waterfall chart --------------------#
s.plt.html(
    order=10,
    html=s.html_components.panel(
        href='https://docs.shimoku.com/development/charts/charts/waterfall',
        text='Waterfall Chart',
        button_panel='Read more',
        symbol_name='insights'
    )
)


data = [
    {'x': 'Nov 1', 'income': 900, 'expenses': 0},
    {'x': 'Nov 2', 'income': 345, 'expenses': 0},
    {'x': 'Nov 3', 'income': 393, 'expenses': 0},
    {'x': 'Nov 4', 'income': 0, 'expenses': 108},
    {'x': 'Nov 5', 'income': 0, 'expenses': 154},
    {'x': 'Nov 6', 'income': 135, 'expenses': 0},
    {'x': 'Nov 7', 'income': 178, 'expenses': 0},
    {'x': 'Nov 8', 'income': 286, 'expenses': 0},
    {'x': 'Nov 9', 'income': 0, 'expenses': 119},
    {'x': 'Nov 10', 'income': 0, 'expenses': 361},
    {'x': 'Nov 11', 'income': 0, 'expenses': 203},
    {'x': 'Nov 12', 'income': 450, 'expenses': 156},
    {'x': 'Nov 13', 'income': 45, 'expenses': 189},
    {'x': 'Nov 14', 'income': 0, 'expenses': 0},
    {'x': 'Nov 15', 'income': 122, 'expenses': 87},
    {'x': 'Nov 16', 'income': 65, 'expenses': 156},
    {'x': 'Nov 17', 'income': 336, 'expenses': 450},
    {'x': 'Nov 18', 'income': 560, 'expenses': 400},
    {'x': 'Nov 19', 'income': 1200, 'expenses': 1130},
    {'x': 'Nov 20', 'income': 3200, 'expenses': 3130},
]

s.plt.waterfall(
    data=data, order=11, x='x',
    positive='income',
    negative='expenses',
)



# -------------------- Title: Heatmap chart -------------------#
s.plt.html(
    order=12,
    html=s.html_components.panel(
        href='https://docs.shimoku.com/development/charts/charts/heatmap',
        text='Heatmap Chart',
        button_panel='Read more',
        symbol_name='insights'
    )
)


data = [
    {
        "xAxis": "Lunes",
        "yAxis": "12 a.m",
        "value": 9
    },
    {
        "xAxis": "Lunes",
        "yAxis": "6 p.m",
        "value": 10
    },
    {
        "xAxis": "Lunes",
        "yAxis": "12 p.m",
        "value": 9
    },
    {
        "xAxis": "Lunes",
        "yAxis": "6 a.m",
        "value": 10
    },
    {
        "xAxis": "Martes",
        "yAxis": "12 a.m",
        "value": 9
    },
    {
        "xAxis": "Martes",
        "yAxis": "6 p.m",
        "value": 9
    },
    {
        "xAxis": "Martes",
        "yAxis": "12 p.m",
        "value": 8
    },
    {
        "xAxis": "Martes",
        "yAxis": "6 a.m",
        "value": 0
    },
    {
        "xAxis": "Miercoles",
        "yAxis": "12 a.m",
        "value": 2
    },
    {
        "xAxis": "Miercoles",
        "yAxis": "6 p.m",
        "value": 7
    },
    {
        "xAxis": "Miercoles",
        "yAxis": "12 p.m",
        "value": 0
    },
    {
        "xAxis": "Miercoles",
        "yAxis": "6 a.m",
        "value": 2
    },
    {
        "xAxis": "Jueves",
        "yAxis": "12 a.m",
        "value": 4
    },
    {
        "xAxis": "Jueves",
        "yAxis": "6 p.m",
        "value": 0
    },
    {
        "xAxis": "Jueves",
        "yAxis": "12 p.m",
        "value": 1
    },
    {
        "xAxis": "Jueves",
        "yAxis": "6 a.m",
        "value": 6
    }
]

s.plt.heatmap(
    data=data, 
    x='xAxis', y='yAxis', 
    values='value', order=13
)



# -------------------- Title: Radar chart -------------------#
s.plt.html(
    order=14,
    html=s.html_components.panel(
        href='https://docs.shimoku.com/development/charts/charts/radar',
        text='Radar Chart',
        button_panel='Read more',
        symbol_name='insights'
    )
)


data = [
    {'name': 'Matcha Latte', 'value1': 78, 'value2': 6, 'value3': 85},
    {'name': 'Milk Tea', 'value1': 17, 'value2': 20, 'value3': 63},
    {'name': 'Cheese Cocoa', 'value1': 57, 'value2': 10, 'value3': 95},
    {'name': 'Walnut Brownie', 'value1': 35, 'value2': 71, 'value3': 16},
]

s.plt.radar(
    data=data, names='name',
    order=15, rows_size=2, cols_size=12,
)



# -------------------- Title: Sunburst chart ------------------#
s.plt.html(
    order=16,
    html=s.html_components.panel(
        href='https://docs.shimoku.com/development/charts/charts/sunburst',
        text='Sunburst Chart',
        button_panel='Read more',
        symbol_name='insights'
    )
)


sunburst_data = [{
    "name": "Root 1",
    "children": [
        {
            "name": "Children A",
            "value": 15,
            "children": [
                {
                    "name": "Children A1",
                    "value": 2
                },
                {
                    "name": "Children AA1",
                    "value": 5,
                    "children": [
                        {
                            "name": "Children AAA1",
                            "value": 2
                        }
                    ]
                },
                {
                    "name": "Children A2",
                    "value": 4
                }
            ]
        },
        {
            "name": "Children B",
            "value": 10,
            "children": [
                {
                    "name": "Children B1",
                    "value": 5
                },
                {
                    "name": "Children B2",
                    "value": 1
                }
            ]
        }
    ]
}, {
    "name": "Root 2",
    "children": [
        {
            "name": "Children A1",
            "children": [
                {
                    "name": "Children AA1",
                    "value": 1
                },
                {
                    "name": "Children AA2",
                    "value": 2
                }
            ]
        }
    ]
}]

s.plt.sunburst(data=sunburst_data, order=17)



# ------------------- Title: Indicators chart ------------------#
s.plt.html(
    order=18,
    html=s.html_components.panel(
        href='https://docs.shimoku.com/development/charts/charts/indicators',
        text='Indicators Chart',
        button_panel='Read more',
        symbol_name='insights'
    )
)


indicators_groups = [
    [
        {
            "description": "% of times the algorithm has predicted the relative position of NY prices with respect to HK prices correctly",
            "title": "Accuracy",
            "value": "76.67%",
            "align": "left",
            "color": "success",
            "variant": "contained"
        },
        {
            "description": "Total of successes predictions",
            "title": "True",
            "value": "154",
            "align": "left",
            "color": "success"
        },
        {
            "description": "Total of Failed predictions",
            "title": "False",
            "value": "22",
            "align": "left",
            "color": "error",
        },
        {
            "description": "Return of investment",
            "title": "ROI",
            "value": "1.5M",
            "align": "left",
            "color": "",
        },
    ]
]

s.plt.indicators_with_header(
    order=19, title='Accuracy', subtitle='Cross-listed trading suite',
    indicators_groups=indicators_groups,
    indicators_parameters=dict(
        cols_size=24,
    )
)


s.run()
#s.terminate_local_server()
 
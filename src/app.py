from dash import Dash, html, dash_tableimport pandas as pd

# Incorporate data
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

app = Dash()

app.layout = [
    html.Div(children='My First App with Data'),
    dash_tanle.DataTable(data=df.to_dict('recods'), page_size=10)
    ]

if __name__ == '__main__':
    app.run(debug=True)
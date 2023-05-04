import pandas as pd
import plotly.express as px

if __name__ == "__main__":

    df = pd.read_csv('csv_file')
#create graph
    fig = px.line(df, x='Temperature', y='Blood_Pressure', title='Temperature with respect to blood pressure')
    fig.show()
#show all data
    print(df.to_string())

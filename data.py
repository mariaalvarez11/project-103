import pandas as pd 
import plotly.express as px

df=pd.read_csv("covid-data.csv")
graph=px.bar(df, x="date", y="cases")
graph.show()
import pandas as pd
import plotly_express as px
df=pd.read_csv("lineChart.csv")
fig=px.line(df, x="Year", y="Per capita income", color="Country", title="Per capita income")
fig.show()
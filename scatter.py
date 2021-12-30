import pandas as pd
import plotly_express as px
df=pd.read_csv("data.csv")
fig=px.scatter(df, x="Population", y="Per capita", color="Country", title="InternetUsers", size="Percentage", size_max=60)
fig.show()
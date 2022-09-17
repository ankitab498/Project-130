import pandas as pa

df = pa.read_csv("project130/data.csv")

del df["Star_name"]


df = df.dropna()

df.to_csv("project130/newData.csv")







import pandas as pd

data = {
    "Name": ["A", "B", "B", None],
    "Score": [90, 85, 85, 70]
}

df = pd.DataFrame(data)

print(df.isnull().sum())

df = df.drop_duplicates()
print(df)

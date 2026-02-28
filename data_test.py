import pandas as pd

data = {
    "sales": [100, 120, 90, 140],
    "month": ["Jan", "Feb", "Mar", "Apr"]
}

df = pd.DataFrame(data)

print(df.describe())

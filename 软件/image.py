import pandas as pd
import requests
import os

df = pd.read_csv("resultado2.csv", encoding="latin1")
df.columns = df.columns.str.strip()

os.makedirs("images", exist_ok=True)

for i, row in df.iterrows():
    artId = str(row['artId'])
    url = row['imageUrl']

    try:
        r = requests.get(url, timeout=10, headers={"User-Agent": "Mozilla/5.0"})
        if r.status_code == 200:
            with open(f"images/{artId}.jpg", "wb") as f:
                f.write(r.content)
            print("OK", artId)
        else:
            print("FAIL", artId)
    except Exception as e:
        print("ERROR", artId, e)
import pandas as pd

df = pd.read_csv("resultado2.csv", encoding="latin1")
df.columns = df.columns.str.strip().str.replace('\ufeff', '')

# 从URL提取 artId 并加 .jpg
df['imageUrl'] = df['imageUrl'].str.split('/').str[5] + ".jpg"

df.to_csv("nuevo.csv", index=False, encoding="utf-8-sig")

print("完成")
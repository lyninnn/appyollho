import pandas as pd

df = pd.read_csv(
    "tianhaodata.csv",
    encoding="latin1"
)

# 清理列名
df.columns = df.columns.str.strip().str.replace('\ufeff', '')

print(df.columns)   # 检查列名

df['categoria'] = df['namees'].where(df['precio'] == 0).ffill()

df.to_csv(
    "resultado.csv",
    index=False,
    encoding="utf-8-sig"
)

print("完成")
import pandas as pd
import math

df = pd.read_csv(
    "resultado.csv",
    encoding="latin1"
)

df.columns = df.columns.str.strip().str.replace('\ufeff', '')

# precio保留2位小数，不四舍五入
df['precio'] = df['precio'].apply(
    lambda x: math.floor(float(x) * 100) / 100
)

# 固定显示2位
df['precio'] = df['precio'].map(lambda x: f"{x:.2f}")

df.to_csv(
    "resultado2.csv",
    index=False,
    encoding="utf-8-sig"
)

print("完成")
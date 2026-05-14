import json
import csv

def build_image_url(artId, imageHash, shopid="071"):
    return f"https://img-eu-2.freex.es/img/{shopid}/{artId}/1024x1024/{imageHash}"

# 读取 JSON
with open("tianhaodata.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# 收集所有 products
products = []
for block in data:
    products.extend(block.get("articulo_lists", []))

fields = ["artId", "namees", "precio", "bianhao", "usercode", "imageUrl"]

# 导出 CSV
with open("tianhaodata.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()

    for item in products:
        new_price = round(item.get("precio", 0) * 1.05, 3)  # 涨价5%

        writer.writerow({
            "artId": item.get("artId", ""),
            "namees": item.get("namees", ""),
            "precio": new_price,
            "bianhao": item.get("bianhao", ""),
            "usercode": item.get("usercode", ""),
            "imageUrl": build_image_url(
                item.get("artId", ""),
                item.get("imageHash", "")
            )
        })

print(f"导出完成，共 {len(products)} 个商品 -> tianhaodata.csv")
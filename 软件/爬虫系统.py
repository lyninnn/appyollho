import json
import csv

def build_image_url(shopid, artId, imageHash):
    return f"https://img-eu-2.freex.es/img/{shopid}/{artId}/1024x1024/{imageHash}"

with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

products = data["articulo_lists"]
shopid = data["shopid"]

fields = ["artId", "namees", "precio", "bianhao", "usercode", "imageUrl"]

with open("output.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()

    for item in products:
        writer.writerow({
            "artId": item.get("artId", ""),
            "namees": item.get("namees", ""),
            "precio": item.get("precio", 0),
            "bianhao": item.get("bianhao", ""),
            "usercode": item.get("usercode", ""),
            "imageUrl": build_image_url(
                shopid,
                item.get("artId", ""),
                item.get("imageHash", "")
            )
        })

print("导出完成：output.csv")
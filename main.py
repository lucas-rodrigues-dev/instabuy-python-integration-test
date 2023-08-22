import csv
import requests

def send_product_to_api(product_data, headers):
    url = "https://api.instabuy.com.br/store/products"
    response = requests.put(url, json=product_data, headers=headers)

headers = {
    "Authorization": "Bearer Mq1EWAXiHwraLIQgfq4stmUxKiM6VpC5Xd9o3wuX1Go"
}

with open('products.csv', 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        product_data = {
            "id": row['Código interno'],
            "name": row['Nome'],
            "brand": row['Código de barras'],
            "pc": [],
            "valid_price": float(row['Preço regular'].replace(',', '.')),
        }
        send_product_to_api(product_data, headers)
        
        print("Produto ID:", product_data["id"])
        print("Nome:", product_data["name"])
        print("Marca:", product_data["brand"])
        print("Preço:", product_data["valid_price"])
        print('-' * 40)
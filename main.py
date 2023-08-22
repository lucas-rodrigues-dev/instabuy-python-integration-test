import csv
import requests

def send_product_to_api(product_data, headers):
    url = "https://api.instabuy.com.br/store/products"
    response = requests.put(url, json=product_data, headers=headers)

api_key = "Mq1EWAXiHwraLIQgfq4stmUxKiM6VpC5Xd9o3wuX1Go"

headers = {
    "api-key": api_key
}

with open('products.csv', 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        price = float(row['Preço regular'].replace(',', '.'))
        formatted_price = f"R${price:.2f}"  # Format to Brazilian currency
        
        product_data = {
            "id": row['Código interno'],
            "name": row['Nome'],
            "brand": row['Código de barras'],
            "pc": [],
            "valid_price": price,
        }
        send_product_to_api(product_data, headers)
        
        print("Produto ID:", product_data["id"])
        print("Nome:", product_data["name"])
        print("Marca:", product_data["brand"])
        print("Preço:", formatted_price)
        print('-' * 40)

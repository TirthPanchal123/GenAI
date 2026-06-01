import requests

product = { 'title':'New Product','price':290}
response = requests.post('https://fakestoreapi.com/products',json=product)
print(response.json())
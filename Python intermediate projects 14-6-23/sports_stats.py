from requests import get
from pprint import PrettyPrinter

BASE_URL = 'https://dummyjson.com/products/category/smartphones'


# ALL_JSON= "/stats/players"



printer=PrettyPrinter()
country = input("Enter a category: ")

url = f'{BASE_URL}/{country}'
data=get(BASE_URL).json()
printer.pprint(data)
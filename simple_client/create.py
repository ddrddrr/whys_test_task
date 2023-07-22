import requests
from random import randint
from client_config import BASE_URL, create, get_model_name
import os
import json

endpoint = BASE_URL + "/import/"

# with open(os.path.abspath(os.path.join('..', 'test_data.json')), mode='r', encoding='utf-8') as td:
# 	test_data = json.load(td)
# 	for payload in test_data:
# 		print(payload)
# 		create(endpoint, payload)
# 		print("------------------")


payload1 = {
	"AttributeName": {
		"id": randint(1, 10000),
		"nazev": "Barva"
	}
}
attrname_id = create(endpoint, payload1)

payload2 = {
	"AttributeValue": {
		"id": randint(1, 10000),
		"hodnota": "hnědá"
	}
}
attrval_id = create(endpoint, payload2)

payload3 = {
	"Product": {
		"id": randint(1, 10000),
		"nazev": "Whirlpool B TNF 5323 OX",
		"description": "Volná stojící kombinovaná lednička se smyslem.",
		"cena": "21566",
		"mena": "CZK",
		"published_on": None,
		"is_published": False
	}
}
product_id = create(endpoint, payload3)

payload4 = {
	"Attribute": {
		"id": randint(1, 10000),
		"nazev_atributu_id": attrname_id,
		"hodnota_atributu_id": attrval_id
	}
}
attribute_id = create(endpoint, payload4)

payload5 = {
	"ProductAttributes": {
		"id": randint(1, 10000),
		"attribute": attribute_id,
		"product": product_id
	}
}
product_attributes_id = create(endpoint, payload5)

from random import randint
from client_config import BASE_URL, get_model_name, create

endpoint = BASE_URL + "/import/"


def create_product_attributes(payload, product_id, attribute_id):
	model_name = get_model_name(payload)
	payload[model_name]['product'] = product_id
	payload[model_name]['attribute'] = attribute_id
	return create(endpoint, payload)


def create_product_image(payload, product_id, image_id):
	model_name = get_model_name(payload)
	payload[model_name]['product'] = product_id
	payload[model_name]['obrazek_id'] = image_id
	return create(endpoint, payload)


def create_catalog(payload, product_ids, attribute_ids, image_id):
	model_name = get_model_name(payload)
	payload[model_name]['products_ids'] = product_ids
	payload[model_name]['attributes_ids'] = attribute_ids
	payload[model_name]['obrazek_id'] = image_id
	return create(endpoint, payload)


payload1 = {
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

payload2 = {
	"ProductAttributes": {
		"id": randint(1, 10000)
	}
}

payload3 = {
	"ProductImage": {
		"id": 2,
		"nazev": "galerie"
	}
}

payload4 = {
	"Catalog": {
		"id": 1,
		"nazev": "Výprodej 2018",
	}
}


def main():
	create_product_attributes(payload2, -1, -2)
	create_product_image(payload3, -1, -1)
	create_catalog(payload4, [], [-1, -1], 5)


main()

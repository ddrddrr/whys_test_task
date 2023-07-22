from random import randint
from client_config import BASE_URL, create, get_model_name

endpoint = BASE_URL + "/import/"


def create_attribute_name(payload):
	return create(endpoint, payload)


def create_attribute_value(payload):
	return create(endpoint, payload)


def create_attribute(payload, attrname_id, attrval_id):
	model_name = get_model_name(payload)
	payload[model_name]['nazev_atributu_id'] = attrname_id
	payload[model_name]['hodnota_atributu_id'] = attrval_id
	return create(endpoint, payload)


def create_attribute_from_scratch():
	attr_name_id = create_attribute_name(payload1)
	attr_val_id = create_attribute_value(payload2)
	return create_attribute(payload3, attr_name_id, attr_val_id)


payload1 = {
	"AttributeName": {
		"id": randint(1, 10000),
		"nazev": "Barva"
	}
}

payload2 = {
	"AttributeValue": {
		"id": randint(1, 10000),
		"hodnota": "hnědá"
	}
}

payload3 = {
	"Attribute": {
		"id": randint(1, 10000),
	}
}


def main():
	attr_name_id = create_attribute_name(payload1)
	attr_val_id = create_attribute_value(payload2)
	create_attribute(payload3, attr_name_id, attr_val_id)


main()

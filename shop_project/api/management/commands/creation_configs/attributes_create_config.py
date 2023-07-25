from .._private import get_model_name, create, faker

payload_attr_name = {
	"AttributeName": {
		"id": faker.pyint(min_value=1, max_value=10000),
		"nazev": faker.word()
	}
}

payload_attr_val = {
	"AttributeValue": {
		"id": faker.pyint(min_value=1, max_value=10000),
		"hodnota": faker.word()
	}
}

payload_attr = {
	"Attribute": {
		"id": faker.pyint(min_value=1, max_value=10000),
	}
}


def create_attribute_name(payload=payload_attr_name):
	return create(payload)


def create_attribute_value(payload=payload_attr_val):
	return create(payload)


def create_attribute(payload=payload_attr):
	model_name = get_model_name(payload)
	payload[model_name]['nazev_atributu_id'] = create_attribute_name(payload_attr_name)
	payload[model_name]['hodnota_atributu_id'] = create_attribute_value(payload_attr_val)
	return create(payload)


mf_map = {
	'attributename': create_attribute_name,
	'attributevalue': create_attribute_value,
	'attribute': create_attribute
}

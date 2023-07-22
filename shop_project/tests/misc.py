from .model_factories import attribute_factory as af, product_factory as pf, image_factory as imgf
import os
import json

IMPORT_ENDPOINT = '/import/'
TEST_DATA = os.path.join("..", 'test_data.json')

FACTORIES = {
	af.AttributeNameFactory,
	af.AttributeValueFactory,
	af.AttributeFactory,
	imgf.ImageFactory,
	pf.ProductFactory,
	pf.ProductAttributesFactory,
	pf.ProductImageFactory,
	pf.CatalogFactory,
}


def get_model_id(payload):
	if isinstance(payload, str):
		payload = json.loads(payload)
	return payload[get_model_name(payload)]['id']


def get_model_name(payload):
	if isinstance(payload, str):
		payload = json.loads(payload)
	return list(payload.keys())[0]


def get_list_endpoint(payload):
	if isinstance(payload, str):
		payload = json.loads(payload)
	return f'/{get_model_name(payload)}/'


def get_detail_endpoint(payload):
	if isinstance(payload, str):
		payload = json.loads(payload)
	return f'{get_list_endpoint(payload)}{get_model_id(payload)}/'

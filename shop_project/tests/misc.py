import os
import json

IMPORT_ENDPOINT = '/import/'
TEST_DATA = os.path.join('..', 'TASK', 'test_data.json')


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

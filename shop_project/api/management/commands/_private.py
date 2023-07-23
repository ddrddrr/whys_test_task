import requests
from faker import Faker, providers

PORT = 8000
BASE_URL = f'http://localhost:{PORT}'
CREATE_ENDPOINT = BASE_URL + '/import/'
faker = Faker()


def create(payload):
	response = requests.post(CREATE_ENDPOINT, json=payload)
	print(response.json())
	try:
		return response.json()['id']
	except Exception as _:
		return -1


def get_model_name(payload):
	try:
		return list(payload.keys())[0]
	except Exception as _:
		return ""


class ModelCreateMixin:
	def create_model(self, model_name, mf_map):
		creation_function = mf_map.get(model_name, None)
		if creation_function:
			mid = creation_function()
			self.stdout.write(self.style.SUCCESS(f'Created {model_name}, id = {mid}'))
		else:
			self.stdout.write(self.style.ERROR(f'Model with name {model_name} does not exist'))

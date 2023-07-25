import requests
from faker import Faker

PORT = 8000
BASE_URL = f'http://localhost:{PORT}'
CREATE_ENDPOINT = BASE_URL + '/import/'
faker = Faker()


def create(payload):
	response = requests.post(CREATE_ENDPOINT, json=payload)
	if response.status_code == 201:
		return list(response.json()['created_objects'].values())[0]
	return -1


def get_model_name(payload):
	try:
		return list(payload.keys())[0]
	except Exception as _:
		return ""


class ModelCreateMixin:
	def create_model(self, model_name, mf_map):
		creation_function = mf_map.get(model_name, None)
		self.create(creation_function, model_name)

	def create(self, create_model, model_name):
		if create_model:
			m_id = create_model()
			if m_id != -1:
				self.stdout.write(self.style.SUCCESS(f'Created {model_name}, id = {m_id}'))
			else:
				self.stdout.write(self.style.ERROR(f'Could not create {model_name}'))
		else:
			self.stdout.write(self.style.ERROR(f'Model with name {model_name} does not exist'))

	def create_all(self, mf_map):
		for model_name, creation_func in mf_map.items():
			self.create(creation_func, model_name)

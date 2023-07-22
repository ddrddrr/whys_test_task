import requests

PORT = 8000
BASE_URL = f'http://localhost:{PORT}'


def create(endpoint, payload):
	response = requests.post(endpoint, json=payload)
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

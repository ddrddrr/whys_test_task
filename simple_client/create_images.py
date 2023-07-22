from client_config import BASE_URL, create

endpoint = BASE_URL + "/import/"


def create_image():
	return create(endpoint, payload1)


payload1 = {
	"Image":
		{
			"id": 6,
			"obrazek": "https://free-images.com/md/faa5/teddy_bear_sheep_toys.jpg"
		}
}
payload2 = {
	"Image": {
		"id": 2,
		"nazev": "plná lednice",
		"obrazek": "https://free-images.com/or/ccc6/faulty_fridge_lighting_led_0.jpg"
	}
}

create(endpoint, payload1)
create(endpoint, payload2)

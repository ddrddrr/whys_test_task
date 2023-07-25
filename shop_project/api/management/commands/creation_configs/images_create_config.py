from .._private import create, faker

payload_image = {
	"Image": {
		"id": faker.pyint(min_value=1, max_value=10000),
		"nazev": faker.word(),
		"obrazek": faker.url()
	}
}


def create_image(payload=payload_image):
	return create(payload)


mf_map = {
	'image': create_image
}


# Test task for whys. Shop API.





## Installation

Docker is needed for the installation

```
1. Clone the project 
    https://github.com/ddrddrr/whys_test_task.git
2. Run this command in root project directory
    docker compose up
```
    
## Usage

```
Base URL is http://localhost:8000/. Same information,
provided below, can be accessed on the this base page.

There are three main endpoints to use:
1. /import/
    Send a POST request with data in form of
    {
      model_name: {
        attr1:val1,
        attr2:val2
        ...
        }
    }
    e.g. 
    {
	  "Product": {
		  "nazev": "Vans old school",
		  "description": "Iconic sneakers",
		  "cena": "1000",
		  "mena": "CZK",
		  "published_on": "23.06.2023",
		  "is_published": false
	  }
  }
  Data should be in JSON format.
  This will create the model, if the data is valid.
  Sample response(JSON) if created:
    {
        'id': 25,
        'url': None,
        'obrazek': 'https://brown.com/', 
        'nazev': 'he'
    }


2. /<model_name>/
    Send a GET request with model name in order to retrieve a list of all
    available model instances

3. /<model_name>/<pk>
    Send a GET request with model name and its pk(in other words - id) in
    order to retrieve the model with this pk.
    Sample response:
    {
        "id": 32,
        "url": "http://localhost:8000/Attribute/32/",
        "nazev_atributu_id": 122,
        "hodnota_atributu_id": 110
    }

4. /<model_name>/detailed
    Same as /<model_name> but nested attributes are written out
    fully instead of id only.

5. /<model_name>/<pk>/detailed
    Same as /<model_name>/<pk> but nested attributes are written out
    fully instead of id only.
```


## Management commands

create_attributes

```
  Creates AttributeName, AttributeValue and Attribute objects with 
  random values. You can provide names explicitly to create only desired models.
  e.g. py manage.py create_attributes AttributeValue
  Model names are case-insensetive
```

create_images

```
  Same as create_attributes, but supports only Image model.
```

create_products

```
  Same as create_attributes, but supports Product, ProductAttributes, ProductImage and Catalog models.
```


## Running Tests

To run tests, run the following command in root 
project folder (where manage.py is located)

```
pytest
```
See pytest documentation for further information about running tests

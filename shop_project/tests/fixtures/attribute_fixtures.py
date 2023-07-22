import pytest


@pytest.fixture
def attribute_name(attribute_name_factory):
	return attribute_name_factory()


@pytest.fixture
def attribute_value(attribute_value_factory):
	return attribute_value_factory()


@pytest.fixture
def attribute(attribute_name, attribute_value, attribute_factory):
	return attribute_factory(
			nazev_atributu=attribute_name,
			hodnota_atributu=attribute_value,
	)


@pytest.fixture
def create_attributes(attribute_name_factory, attribute_value_factory, attribute_factory):
	ids = [1, 2, 3]

	attributes = []
	for curr_id in ids:
		attribute_name = attribute_name_factory(id=curr_id)
		attribute_value = attribute_value_factory(id=curr_id)
		attribute = attribute_factory(nazev_atributu=attribute_name, hodnota_atributu=attribute_value)
		attributes.append(attribute)

	return attributes

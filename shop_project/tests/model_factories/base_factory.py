import factory
from factory.django import DjangoModelFactory


class UserIdFactory(DjangoModelFactory):
	id = factory.Sequence(lambda n: n + 1)  # counter starts at 0, hence +1 for assertions

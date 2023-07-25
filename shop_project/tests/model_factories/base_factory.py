from factory.django import DjangoModelFactory
import factory


class UserIdFactory(DjangoModelFactory):
	id = factory.Sequence(lambda n: n + 1)  # counter starts at 0, hence +1 for assertions

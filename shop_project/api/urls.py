from django.urls import path
from .views import ModelCreateView, ModelListView, ModelRetrieveView, DetailedModelRetrieveView, \
	DetailedModelListView, api_home

urlpatterns = [
	path('', api_home, name='api-home'),
	path('import/', ModelCreateView.as_view(), name='model-create'),
	path('<str:model_name>/<int:pk>/detailed', DetailedModelRetrieveView.as_view(), name='detailed-retrieve'),
	path('<str:model_name>/<int:pk>/', ModelRetrieveView.as_view(), name='model-retrieve'),
	path('<str:model_name>/detailed/', DetailedModelListView.as_view(), name='detailed-list'),
	path('<str:model_name>/', ModelListView.as_view(), name='model-list'),
]

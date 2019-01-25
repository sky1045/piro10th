from django.urls import path
from .views import *

urlpatterns = [
	path('', list_article, name='list'),
	path('<int:pk>/', detail_article, name='detail'),
	path('create/', create_article, name='create'),
	]

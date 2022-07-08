from django.views.decorators.csrf import csrf_exempt
from django.urls import path, include

from . import views

urlpatterns = [
	path('', csrf_exempt(views.main_page)),
	path('history/', views.history_page),
	path('clients/<int:pk>', views.ClientsDetailView.as_view()),
	path('books/<int:pk>', views.BooksDetailView.as_view())
]
from re import template
from webbrowser import Opera
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponse
import json

from .models import *

def main_page(request):
	books = Books.objects.all()
	clients = Clients.objects.all()
	actions = Actions.objects.all()

	if request.method == 'POST':
		opf = request.POST.get("operations-form-submit")

		if opf:
			selected_book = request.POST.get("books-select")
			selected_client = request.POST.get("clients-select")
			selected_action = request.POST.get("actions-select")
			selected_client_obj = Clients.objects.get(name=selected_client)	
			if selected_book and selected_action and selected_client:
				operationsModel = Operations.objects.create(client=selected_client_obj, options=Actions.objects.get(id=selected_action), book=Books.objects.get(id=selected_book))

				if int(selected_action) == 1:
					restrictions = Books.objects.get(id=selected_book)
					if restrictions.number_of_books > 0:
						client = Clients.objects.get(name=selected_client)
						client.books.add(selected_book)
						client.save()

						change_book_amount = Books.objects.get(id=selected_book)
						change_book_amount.number_of_books -= 1
						change_book_amount.save()
					else:
						return HttpResponse("<script>alert('No Books')</script>")
						
						

				elif int(selected_action) == 2:
					client = Clients.objects.get(name=selected_client)
					client.books.remove(selected_book)
					client.save()

					change_book_amount = Books.objects.get(id=selected_book)
					change_book_amount.number_of_books += 1
					change_book_amount.save()

				return redirect('/')

		elif json.loads(request.body).get('searchBooks'):
			books_search_bar = json.loads(request.body).get('searchBooks')
			result = Books.objects.filter(title__icontains=books_search_bar)
			data = result.values()
			return JsonResponse(list(data), safe=False)

		elif json.loads(request.body).get('searchClients'):
			clients_search_bar = json.loads(request.body).get('searchClients')
			result = Clients.objects.filter(name__icontains=clients_search_bar)
			data = result.values()
			return JsonResponse(list(data), safe=False)

		
	return render(request, 'main/main_page.html', {'books': books, 'clients': clients, 'actions': actions})

def history_page(request):
	if request.method == "GET":
		search_bar = request.GET.get("searchBar")
		order_sortering_bar = request.GET.get("by_order")
		date_filtering_bar = request.GET.get("history-date-filter")
		filtered_operations = Operations.objects.all()

		#FILTER IF STATEMENTS
		if search_bar and order_sortering_bar:
			if order_sortering_bar == "older":
				filtered_operations = Operations.objects.filter(book__title__icontains=search_bar).order_by("-time_of_operation") | Operations.objects.filter(client__name__icontains=search_bar).order_by("-time_of_operation")
			elif order_sortering_bar == "newer":
				filtered_operations = Operations.objects.filter(book__title__icontains=search_bar).order_by("time_of_operation") | Operations.objects.filter(client__name__icontains=search_bar).order_by("time_of_operation")
			else:
				pass
		elif search_bar and date_filtering_bar:
			filtered_operations = Operations.objects.filter(book__title__icontains=search_bar, time_of_operation__icontains=date_filtering_bar) | Operations.objects.filter(client__name__icontains=search_bar, time_of_operation__icontains=date_filtering_bar)
		elif order_sortering_bar and date_filtering_bar:
			if order_sortering_bar == "older":
				filtered_operations = Operations.objects.filter(time_of_operation__icontains=date_filtering_bar).order_by("-time_of_operation")
			elif order_sortering_bar == "newer":
				filtered_operations = Operations.objects.filter(time_of_operation__icontains=date_filtering_bar).order_by("time_of_operation")
			else:
				pass
		elif order_sortering_bar:
			if order_sortering_bar == "older":
				filtered_operations = Operations.objects.all().order_by("-time_of_operation")
			elif order_sortering_bar == "newer":
				filtered_operations = Operations.objects.all().order_by("time_of_operation")
			else:
				pass
		elif date_filtering_bar:
			filtered_operations = Operations.objects.filter(time_of_operation__icontains=date_filtering_bar)
		elif search_bar:
			filtered_operations = Operations.objects.filter(book__title__icontains=search_bar) | Operations.objects.filter(client__name__icontains=search_bar)
		
		return render(request, "main/history_page.html", {'operations': filtered_operations})
		
	operations_model = Operations.objects.all()
	return render(request, "main/history_page.html", {'operations': operations_model})

class ClientsDetailView(DetailView):
	model = Clients
	template_name = 'detail/clients_detail.html'

class BooksDetailView(DetailView):
	model = Books
	template_name = 'detail/books_detail.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['clients'] = Clients.objects.filter(books = self.object)
		return context


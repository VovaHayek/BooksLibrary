from django.db import models
from django.utils import timezone

class Books(models.Model):
	title = models.CharField(max_length=100)
	author = models.CharField(max_length=100)
	number_of_books = models.IntegerField()

	def __str__(self):
		return self.title

class Clients(models.Model):
	name = models.CharField(max_length=120)
	phone = models.CharField(max_length=15, unique=True)
	birth_date = models.DateField(null=True)
	books = models.ManyToManyField(Books)

	def __str__(self):
		return self.name

class Actions(models.Model):
	action_name = models.CharField(max_length=100)

	def __str__(self):
		return self.action_name

class Operations(models.Model):
	id = models.AutoField(primary_key=True, unique=True)
	book = models.ForeignKey(Books, null=True, on_delete=models.PROTECT)
	client = models.ForeignKey(Clients, null=True, on_delete=models.CASCADE)
	options = models.ForeignKey(Actions, null=True, on_delete=models.CASCADE)
	time_of_operation = models.DateTimeField(default=timezone.now())

	def __str__(self):
		return self.client.name

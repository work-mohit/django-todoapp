from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import tododata

# Create your views here.
def home(request):
	context = {
        'todoItem' : tododata.objects.all()
    }
	return render(request ,"TodoList/home.html", context)

class TodoItemListView(ListView):
	model = tododata
	template_name = 'TodoList/home.html'
	context_object_name ='todoItem' 

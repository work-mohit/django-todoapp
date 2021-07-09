from django.urls.conf import include
from . import views
from django.urls import path
from .views import TodoItemListView

urlpatterns = [
    # path('',views.home,name='home')
    path('',TodoItemListView.as_view(), name='home')
]

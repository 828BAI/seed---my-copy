from django.urls import path, include

from .views import (ProjectListView , ProjectDetailView)

urlpatterns =[
    path('',ProjectListView.as_view()),
    path('<pk>',ProjectDetailView.as_view()),
    

]



from django.contrib import admin
from django.urls import path,include
from . import views
from .views import RegisterView, RetrieveUserView
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('users/register',   name='register'),
  
    path('me', RetrieveUserView.as_view()),
    path('register', RegisterView.as_view()),
    ]
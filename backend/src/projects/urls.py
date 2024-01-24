from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import ManageProjectView, ProjectDetailView, ProjectsView, SearchProjectsView

urlpatterns = [
   path('manage', ManageProjectView.as_view()),
    path('allprojects', ManageProjectView.as_view()),
    path('<slug:slug>', ProjectDetailView.as_view()),
    path('search', SearchProjectsView.as_view()),
  
    
]

urlpatterns +=static(settings.MEDIA_URL, document_rook = settings.MEDIA_ROOT)
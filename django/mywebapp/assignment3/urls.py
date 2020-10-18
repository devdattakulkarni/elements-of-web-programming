from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('libraries', views.handle_libraries, name='handle_libraries'),
    path('libraries/<int:library_id>', views.handle_single_library, name='handle_single_library'),
]


from django.urls import path
from tenant_library import views



urlpatterns = [
   
    path('index/',views.index),
    path('create',views.library_create),
    path('update',views.library_update),
    path('delete',views.library_delete),

]
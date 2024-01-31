from django.urls import path

from . import views


urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('filter/', views.ClientesFilterView.as_view(), name='filter_client'),
    path('create/', views.ClienteCreateView.as_view(), name='create_client'),
    path('update/<int:pk>', views.ClienteUpdateView.as_view(), name='update_client'),
    path('read/<int:pk>', views.ClienteReadView.as_view(), name='read_client'),
    path('delete/<int:pk>', views.ClienteDeleteView.as_view(), name='delete_client'),
    path('clientes/', views.clientes, name='clientes'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
]
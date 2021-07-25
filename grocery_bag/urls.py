
from django.urls import path


from .views import (
    GroceryUpdateView,
    GroceryDeleteView,
    GroceryCreateView,
    groceries_home, 
    ContactView,
    AboutView
)

app_name = 'g_bag'
urlpatterns = [
    path('', groceries_home, name='home'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('about/', AboutView.as_view(), name='about'),
    path('grocery/new/', GroceryCreateView.as_view(), name='grocery_new'),
    path('grocery/<int:pk>/edit/', 
        GroceryUpdateView.as_view(), name='grocery_edit'),
    path('grocery/<int:pk>/delete/', 
        GroceryDeleteView.as_view(), name='grocery_delete'), 

]




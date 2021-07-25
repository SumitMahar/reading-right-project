from django.views.generic import TemplateView
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    UpdateView, DeleteView, CreateView
)
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from .models import Grocery


class HomeView(TemplateView):
    '''
        Since we do not need to render any dynamic data
        django's builtin class based view takes care of this for us.
    '''
    # we only have to specify the template name 
    template_name = 'grocery_bag/home.html'


class AboutView(TemplateView):
    template_name = 'grocery_bag/about.html'


class ContactView(TemplateView):
    template_name = 'grocery_bag/contact.html'


# Utility functions
def check_grocery_owner(request, grocery):
    ''' Raises 404 error if the topic owner is not the request.user '''

    if request.user != grocery.owner:
        raise Http404()

def groceries_home(request):
    """Show all groceries of a specific user """
    # If user is unauthenticated then only show him Public posts if any
    if not request.user.is_authenticated:
        return render(request, "grocery_bag/home.html")

    # If authenticated then return all the topics belonging to the user
    grocery_list = Grocery.objects.filter(owner=request.user).order_by("-date")

    context = {"grocery_list": grocery_list}
    context['bought_items'] = Grocery.objects.filter(owner=request.user, item_status='BOUGHT').count()
    context['pending_items'] = Grocery.objects.filter(owner=request.user, item_status='PENDING').count()
    context['not_available'] = Grocery.objects.filter(owner=request.user, item_status='NOT-AVAILABLE').count()

    return render(request, "grocery_bag/home.html", context)


class GroceryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Grocery 
    context_object_name = 'grocery'
    fields = ('item_name', 'item_quantity', 'item_status')
    template_name = 'grocery_bag/grocery_edit.html'

    # this is to test whether the owner of the grocery is the actual loged in user
    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user


class GroceryCreateView(LoginRequiredMixin, CreateView):
    model = Grocery 
    template_name = 'grocery_bag/add_grocery.html'
    fields = ('item_name', 'item_quantity', 'item_status')
    success_url = reverse_lazy('g_bag:home')


    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class GroceryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Grocery
    context_object_name = 'grocery'
    template_name = 'grocery_bag/grocery_delete.html'
    success_url = reverse_lazy('g_bag:home')

    # this is to test whether the owner of the grocery is the actual loged in user
    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user
        



from django.views.generic import ListView
from django.views import generic
from groups.models import Group


class HomePageView(generic.ListView):
    model = Group
    template_name = 'home/index.html'
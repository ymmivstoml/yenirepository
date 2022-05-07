from django.shortcuts import render
from django.views.generic import CreateView,TemplateView,ListView
from theapp.models import Dumdatas
from theapp.forms import DataForm
from django.utils import timezone


# Create your views here.


class HomePage(TemplateView):
    template_name = 'index.html'



class DataCreation(CreateView):
    template_name = "dumdatas_form.html"

    model = Dumdatas
    form_class = DataForm

    

class DataListView(ListView):
    template_name = "data_list.html"

    model = Dumdatas

    def get_queryset(self):
        return Dumdatas.objects.filter(zaman__lte=timezone.now()).order_by('-zaman')

from django.views.generic.edit import CreateView, UpdateView, DeleteView
#from django.views.generic.base import RedirectView
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from .models import Student


def index(request):
    return render(request, 'crud_app/index.html')


def contact(request):
    return render(request, 'crud_app/contact.html')


def delete_confirm(request):
    return render(request, 'crud_app/student_delete_confirmed.html')


class ListView(generic.ListView):
    template_name = 'crud_app/list_all.html'
    context_object_name = 'all_students'

    def get_queryset(self):
        return Student.objects.all()


class DetailView(generic.DetailView):
    model = Student
    template_name = 'crud_app/detail.html'


class StudentCreate(CreateView):
    model = Student
    fields = ['Surname', 'Firstname', 'Department', 'Level', 'email', 'age', 'Phone_number']
    success_url = reverse_lazy('crud_app:all_list')


class StudentUpdate(UpdateView):
    model = Student
    fields = ['Surname', 'Firstname', 'Department', 'Level', 'email', 'age', 'Phone_number']
    success_url = reverse_lazy('crud_app:all_list')


class StudentDelete(DeleteView):
    model = Student
    success_url = reverse_lazy('crud_app:index')


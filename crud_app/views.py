from django.shortcuts import render


def index(request):
    return render(request, 'crud_app/index.html')
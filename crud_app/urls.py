from django.conf.urls import url
from . import views

app_name = 'crud_app'

urlpatterns = [
    # /students/
    url(r'^$', views.index, name='index'),

]

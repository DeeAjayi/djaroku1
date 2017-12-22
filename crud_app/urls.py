from django.conf.urls import url
from . import views

app_name = 'crud_app'

urlpatterns = [
    # /students/
    url(r'^$', views.index, name='index'),

    # /students/id<1>
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # /students/add
    url(r'add/$', views.StudentCreate.as_view(), name='student-add'),

    # /students/update/<pk>
    url(r'update/(?P<pk>[0-9]+)/$', views.StudentUpdate.as_view(), name='student-update'),

    # /students/delete/<pk>/
    url(r'delete/(?P<pk>[0-9]+)/$', views.StudentDelete.as_view(), name='student-delete'),

    # /students/all/
    url(r'all/$', views.ListView.as_view(), name='all_list'),

    # /students/contact
    url(r'contact/$', views.index, name='contact'),

    # /students/delete/confirm/
    url(r'delete/confirm/$', views.delete_confirm, name='delete-confirm'),

]

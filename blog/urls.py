from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='blog-home'),
    path('about/',views.about,name='blog-about'),
    path('table/',views.table,name='blog-table'),
    path('index/',views.index,name='index'),
    path('info/',views.info,name='info')
    
    
]

from django.urls import path
from .views import index,doctor_detail,services,service_detail,doctors,blog,blog_detail,contact,appointment,table,success,about,blog_search


urlpatterns = [
    path('',index, name='index'),
    path('doctors/',doctors, name='doctors'),
    path('doctor/<int:pk>/',doctor_detail, name='doctor_detail'),
    path('services/',services, name='services'),
    path('service_detail/',service_detail, name='service_detail'),
    path('blog/',blog, name='blog'),
    path('blog/<int:post_id>/',blog_detail, name='blog_detail'),
    path('blog/search/',blog_search, name='blog_search'),
    path('contact/',contact, name='contact'),
    path('appointment/',appointment, name='appointment'),
    path('table/',table, name='table'),
    path('success/',success, name='success' ),
    path('about/',about, name='about' ),
]

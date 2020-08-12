from django.urls import path
from .views import home,project_detail,contact,portfolio,services,About, pdf_resume


app_name = 'first_app'

urlpatterns = [
    path('',home,name='home'),
    path('portfolio',portfolio,name='portfolio'),
    path('about',About,name='about'),
    path('services/',services,name='services'),
    path('contact/',contact,name='contact'),
    path('project_detail/<slug>',project_detail,name='project_detail'),
    path('pdf',pdf_resume,name='pdf'),
]
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('E_commerce/', views.E_commerce, name='E_commerce'),
    path('elements/', views.elements, name='elements'),
    path('erp_development/', views.erp_development, name='erp_development'),
    path('Graphic_design/', views.Graphic_design, name='Graphic_design'),
    path('internet_marketing/', views.internet_marketing, name='internet_marketing'),
    path('mobile_app_development/', views.mobile_app_development, name='mobile_app_development'),
    path('multivendor/', views.multivendor, name='multivendor'),
    path('open_source_development/', views.open_source_development, name='open_source_development'),
    path('services/', views.services, name='services'),
    path('software_solutions/', views.software_solutions, name='software_solutions'),
    path('traning/', views.traning, name='traning'),
    path('web_application/', views.web_application, name='web_application'),
    path('web_development/', views.web_development, name='web_development'),
    path('web_hosting/', views.web_hosting, name='web_hosting'),
    path('projects/', views.projects, name='projects'),
    path('career/', views.career, name='career'),
    path('contact/', views.contact, name='contact'),

  
]

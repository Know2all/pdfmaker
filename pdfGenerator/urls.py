from django.urls import path
from .import views

urlpatterns = [
    path('generate',views.generate_pdf_from_url,name='generate-pdf'),
    path('test',views.test,name='test'),
]
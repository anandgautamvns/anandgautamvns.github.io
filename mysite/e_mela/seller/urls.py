from django.urls import path
from seller import views

app_name = 'seller'
urlpatterns = [
    path('upload_product', views.upload_product, name='upload_product'),
]

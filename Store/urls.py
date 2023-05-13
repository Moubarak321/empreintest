from django.urls import path
from . import views

urlpatterns = [
  
    # path('vehicules/', views.vehicules , name = "vehicules" ),  
    path('a-propos/', views.a_propos , name = "a-propos" ),  
    # path('voiture/<str:slug>', views.voiture , name = "voiture" ),  
    path('reserver', views.reserver , name = "reserver" ),  
    path('services', views.service , name = "service" ),  
    path('benin_mobilier', views.meubles , name = "meubles" ),  
    path('gallerie', views.gallerie , name = "gallerie" ),  
    path('contacter', views.contacter , name = "contacter" ),  
    # path('contact', views.contact , name = "contact" ),
] 

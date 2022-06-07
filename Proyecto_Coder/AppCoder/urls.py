from django.urls import path
from AppCoder.views import profesores,curso, plantilla1


urlpatterns = [
   path('profesores/', profesores),
   path('curso/', curso), 
   path('plantilla1/', plantilla1), 
    
]


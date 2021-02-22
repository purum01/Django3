from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile),
    path('signup/', views.signup, name='signup' )
]

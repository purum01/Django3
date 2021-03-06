from django.urls import path, register_converter
from . import views
from .converters import CodeConverter

register_converter(CodeConverter, 'code')

urlpatterns = [
    path('', views.list),
    path('<int:id>/', views.detail),
    path('tag/<id>/', views.tag_list),
    path('test1/', views.test1),
    path('test2/<int:no>/', views.test2),
    path('test3/<year>/<month>/<day>/', views.test3),
    path('test4/<code:id>/', views.test4),
    path('test5/', views.test5),
    path('test6/', views.test6),
]

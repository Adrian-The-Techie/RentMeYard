from django.urls import path
from . import views

urlpatterns=[
    path("", views.index, name="index"),
    path('services/', views.services, name='services'),
    path('services/<str:url>', views.specificService, name="specificService"),
    path('report', views.report, name="report"),
    path('comment', views.comment, name="comment"),
    path('categories/<int:id>', views.filterByCategory, name="filterByCategory"),
    path('searchForServices', views.searchForServices, name="searchForServices"),
    path('api/', views.api, name='api')
]
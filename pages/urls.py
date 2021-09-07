from django.urls import path
from .views import HomePageView,AboutPageView,Base

urlpatterns = [
    path('',HomePageView.as_view(), name='home'),
    path('base/',Base.as_view(),name='base'),
    path('about/',AboutPageView.as_view(),name='about'),
]

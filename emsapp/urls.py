from django.urls import path
from emsapp import views

urlpatterns = [
    path('',views.home ),
    path("search/", views.searchbar, name='search'),
    path("leave_request/",views.leave_request),
    path("leave_status/",views.leave_status),

]

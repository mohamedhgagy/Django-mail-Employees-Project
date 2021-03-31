from django.urls import path
from .views import login,register,emp,contact,log_out
urlpatterns = [
    path('login/',login,name='login'),
    path('',register,name='signup'),
    path('index/',emp,name='index'),
    path('contact/<int:id>',contact,name='contact'),
    path('logout/',log_out,name='logout')
]

from django.urls import path
from . import views

urlpatterns = [
    path('add_data/', views.add_data, name='add_data'),
    path('show_data/', views.show_data, name='show_data'),
    path('add_signal/', views.post_signal, name='post_signal'),
    path('show_signals/', views.show_signals, name='show_signals'),
]

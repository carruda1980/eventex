from django.urls import path

from eventex.subscriptions.views import subscribe, detail

app_name = 'subscriptions'

urlpatterns = [
    path('inscricao/', subscribe, name='new'),
    path('inscricao/<int:pk>/', detail, name='detail'),
]
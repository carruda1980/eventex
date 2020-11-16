from django.urls import path

from eventex.subscriptions.views import subscribe, detail

urlpatterns = [
    path('inscricao/', subscribe),
    path('inscricao/<int:pk>/', detail),
]
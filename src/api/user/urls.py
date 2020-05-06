from django.urls import (
    include,
    path,
)
from user import views 


urlpatterns = [
    path('', views.UsersView.as_view()),
]

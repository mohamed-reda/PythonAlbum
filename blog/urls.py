from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'main_app'
urlpatterns = [
    # path('home/', TemplateView.as_view(template_name="home.html"), )
    path('', views.home, name="homepage")

]

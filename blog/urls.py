from django.urls import path
from django.views.generic import TemplateView
app_name = 'main_app'
urlpatterns = [
    path('', TemplateView.as_view(template_name="home.html"), )

]

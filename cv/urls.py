from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = "cv"

urlpatterns = [
    path("", views.home, name="home"),
    path("contact/", views.contact, name="contact"),
    path("resume/", views.resume_download, name="resume"),
    path("sitemap.xml", views.sitemap, name="sitemap"),
    path("privacy/", TemplateView.as_view(template_name="cv/privacy.html"), name="privacy"),
]

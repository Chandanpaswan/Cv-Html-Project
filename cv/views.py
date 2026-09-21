from django.contrib import messages
from django.http import FileResponse, Http404, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils import timezone
from django.utils.feedgenerator import Rss201rev2Feed
from django.views.decorators.http import require_POST

from blog.models import BlogPost
from .forms import ContactForm
from .models import (AboutSection, Achievement, Certification, Education, Experience,
                     PersonalInformation, Project, SEOSettings, Service, Skill, SocialLink)


def _profile():
    return PersonalInformation.objects.filter(is_active=True).first() or PersonalInformation()


def home(request):
    profile = _profile()
    seo = SEOSettings.objects.filter(page_key="home").first()
    context = {
        "profile": profile,
        "about": AboutSection.objects.filter(is_visible=True).first(),
        "experiences": Experience.objects.filter(is_visible=True),
        "education": Education.objects.filter(is_visible=True),
        "skills": Skill.objects.filter(is_visible=True),
        "services": Service.objects.filter(is_visible=True),
        "projects": Project.objects.filter(is_visible=True),
        "certifications": Certification.objects.filter(is_visible=True),
        "achievements": Achievement.objects.filter(is_visible=True),
        "social_links": SocialLink.objects.filter(is_visible=True),
        "latest_posts": BlogPost.objects.filter(is_published=True)[:3],
        "seo": seo,
        "contact_form": ContactForm(),
    }
    return render(request, "cv/home.html", context)


@require_POST
def contact(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, "Thanks. Your enquiry has been received.")
        return redirect(f"{reverse('cv:home')}#contact")
    profile = _profile()
    return render(request, "cv/home.html", {"profile": profile, "contact_form": form}, status=400)


def resume_download(request):
    profile = _profile()
    if not profile.cv_file:
        raise Http404("A CV file has not been uploaded yet.")
    return FileResponse(profile.cv_file.open("rb"), as_attachment=True, filename=profile.cv_file.name.split("/")[-1])


def sitemap(request):
    pages = [request.build_absolute_uri(reverse("cv:home")), request.build_absolute_uri(reverse("blog:list"))]
    posts = [request.build_absolute_uri(post.get_absolute_url()) for post in BlogPost.objects.filter(is_published=True)]
    urls = "".join(f"<url><loc>{url}</loc></url>" for url in pages + posts)
    return HttpResponse(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>', content_type="application/xml")

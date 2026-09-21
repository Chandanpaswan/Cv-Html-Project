from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render

from blog.models import BlogPost
from cv.models import (Achievement, Certification, ContactMessage, Education, Experience,
                       PersonalInformation, Project, Service, Skill)


@staff_member_required
def home(request):
    profile = PersonalInformation.objects.first()
    stats = [
        ("Experiences", Experience.objects.count(), "experience"),
        ("Projects", Project.objects.count(), "project"),
        ("Skills", Skill.objects.count(), "skill"),
        ("Unread messages", ContactMessage.objects.filter(is_read=False).count(), "message"),
    ]
    counts = {
        "education": Education.objects.count(),
        "services": Service.objects.count(),
        "certifications": Certification.objects.count(),
        "achievements": Achievement.objects.count(),
        "blog_posts": BlogPost.objects.count(),
    }
    return render(request, "dashboard/index.html", {"profile": profile, "stats": stats, "counts": counts, "recent_posts": BlogPost.objects.order_by("-created_at")[:5]})

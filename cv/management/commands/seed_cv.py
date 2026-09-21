from datetime import date, datetime, time

from django.core.management.base import BaseCommand
from django.utils import timezone

from blog.models import BlogPost
from cv.models import (AboutSection, Achievement, Certification, Education, Experience,
                       PersonalInformation, Project, SEOSettings, Service, Skill, SocialLink)


class Command(BaseCommand):
    help = "Seed the CV website with Chandan's initial profile content."

    def handle(self, *args, **options):
        PersonalInformation.objects.update_or_create(pk=1, defaults={
            "name": "Chandan Kumar Paswan",
            "title": "SEO & Digital Marketing Specialist",
            "short_intro": "I help ambitious businesses become easier to find, trust, and choose through technical SEO, sharp content, and digital experiences that convert.",
            "email": "Paswan.chandan75@gmail.com",
            "phone": "+91 70159 07650",
            "whatsapp_number": "917015907650",
            "location": "India",
            "years_experience": "5+",
            "traffic_growth": "20%",
            "ranking_improvement": "30+",
            "task_completion": "98%",
            "available_for_work": True,
            "is_active": True,
        })
        AboutSection.objects.update_or_create(pk=1, defaults={
            "title": "Curious by nature. Precise by practice.",
            "lead": "I turn search data and business goals into clear, compounding growth.",
            "body": "I am Chandan, an SEO and digital marketing specialist who enjoys the point where strategy meets execution. From technical audits and keyword architecture to content systems and performance reporting, I build practical growth programs that teams can actually use.",
            "is_visible": True,
        })
        Experience.objects.update_or_create(company="iEve Era Pvt. Ltd.", role="SEO Specialist", defaults={
            "location": "Mumbai", "start_date": date(2022, 8, 1), "end_date": date(2023, 6, 1),
            "responsibilities": "Built and implemented SEO strategies that increased organic traffic by 20%.\nLed technical audits, keyword analysis, rank strategy, and reporting across multiple domains.\nCollaborated with content and project teams while managing 1-6 daily projects at a 98% completion rate.",
            "tools": "Semrush, Search Console, Google Analytics, Technical SEO", "sort_order": 1, "is_visible": True,
        })
        Experience.objects.update_or_create(company="AskmeClassified", role="SEO Executive", defaults={
            "location": "Delhi", "start_date": date(2020, 6, 1), "end_date": date(2021, 6, 1),
            "responsibilities": "Lifted organic traffic by 20% through on-page optimization and backlink campaigns.\nImproved CTR with stronger titles, meta descriptions, and anchor text.\nResolved indexing issues and ran competitive analysis that contributed to an 18% increase in converting visitors.",
            "tools": "On-page SEO, Keyword research, Analytics, Link building", "sort_order": 2, "is_visible": True,
        })

        skills = [
            ("SEO strategy", "SEO", "Keyword research, content architecture, SERP opportunity mapping.", 96),
            ("Technical SEO", "SEO", "Crawling, indexing, Core Web Vitals, schema, and site health.", 91),
            ("On-page & off-page", "SEO", "Metadata, internal linking, content optimization, and authority.", 94),
            ("Analytics & Ads", "Analytics", "Google Analytics, Search Console, reporting, and Google Ads.", 84),
            ("Web development", "Development", "HTML, CSS, JavaScript, WordPress, and conversion-ready UX.", 78),
            ("AI-powered marketing", "AI", "Smarter research, content workflows, and efficient experimentation.", 81),
        ]
        for order, (name, category, description, proficiency) in enumerate(skills, 1):
            Skill.objects.update_or_create(name=name, defaults={"category": category, "description": description, "proficiency": proficiency, "sort_order": order, "is_visible": True})

        services = [
            ("SEO growth", "Research-led strategy that creates durable visibility."),
            ("Website optimization", "Technical fixes and UX improvements that remove friction."),
            ("Google Ads", "Sharper targeting, landing pages, and measurable acquisition."),
            ("Technical audits", "Clarity on the issues holding your search performance back."),
        ]
        for order, (name, description) in enumerate(services, 1):
            Service.objects.update_or_create(name=name, defaults={"description": description, "sort_order": order, "is_visible": True})

        projects = [
            ("Search visibility sprint", "SEO", "A technical and content reset for a classified marketplace, built around high-intent queries.", "Technical audit, Content strategy", "+20% organic traffic / +18% conversions", "https://askmeclassified.com"),
            ("Nxtwalk digital presence", "Web", "A conversion-focused web presence paired with a search foundation designed to compound.", "WordPress, SEO, UX", "Clearer positioning / stronger organic foundation", "https://www.nxtwalk.in/"),
        ]
        for order, (name, category, description, tools, result, live_url) in enumerate(projects, 1):
            Project.objects.update_or_create(name=name, defaults={"category": category, "description": description, "tools": tools, "result": result, "live_url": live_url, "sort_order": order, "is_visible": True})

        education = [
            ("Pt. L R Group of Institutions", "Diploma / Mechanical Engineering", "A systems-oriented technical education that informs how I approach digital problems today.", 2023),
            ("Govt Boys Senior Secondary School", "Senior Secondary Education", "A strong base in research, communication, and disciplined execution.", 2018),
        ]
        for order, (institution, qualification, description, end_year) in enumerate(education, 1):
            Education.objects.update_or_create(institution=institution, qualification=qualification, defaults={"description": description, "end_year": end_year, "sort_order": order, "is_visible": True})

        Certification.objects.update_or_create(name="SEO & performance marketing practice", defaults={"issuer": "Professional training", "description": "Applied learning across Google Analytics, Search Console, Semrush, email marketing, and social media strategy.", "sort_order": 1, "is_visible": True})
        Achievement.objects.update_or_create(title="20% organic traffic growth delivered", defaults={"description": "Repeatedly improved visibility through practical on-page, technical, and off-page SEO work.", "year": 2023, "sort_order": 1, "is_visible": True})
        SocialLink.objects.update_or_create(platform="LinkedIn", defaults={"label": "LinkedIn", "url": "https://www.linkedin.com/in/seo-chandanpaswan/", "sort_order": 1, "is_visible": True})
        SocialLink.objects.update_or_create(platform="Website", defaults={"label": "Nxtwalk", "url": "https://www.nxtwalk.in/", "sort_order": 2, "is_visible": True})
        SEOSettings.objects.update_or_create(page_key="home", defaults={"title": "Chandan Kumar Paswan | SEO & Digital Marketing Specialist", "meta_description": "SEO, web development and digital marketing strategies that turn search intent into measurable growth.", "keywords": "SEO specialist, digital marketing, technical SEO, web development, Chandan Paswan", "canonical_url": "https://www.chandanpaswan.com/"})
        published_at = timezone.make_aware(datetime.combine(date(2026, 9, 12), time.min))
        BlogPost.objects.update_or_create(slug="technical-seo-growth-discipline", defaults={"title": "Why technical SEO is a growth discipline", "excerpt": "Technical work is most valuable when it connects directly to user experience and commercial intent.", "content": "Healthy crawling, clear information architecture, and fast templates make every content investment more discoverable. The best audit is the one that ends with an ordered, owned action list.", "category": "SEO", "tags": "technical SEO, growth, audits", "published_at": published_at, "is_featured": True, "is_published": True})
        self.stdout.write(self.style.SUCCESS("CV content seeded successfully. Upload photos and documents through the admin dashboard."))

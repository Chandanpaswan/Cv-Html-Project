from datetime import date, datetime, time

from django.core.management.base import BaseCommand
from django.utils import timezone

from blog.models import BlogPost
from cv.models import (AboutSection, Achievement, Certification, Education, Experience,
                       PersonalInformation, Project, SEOSettings, Service, Skill, SocialLink)


class Command(BaseCommand):
    help = "Seed the CV website with Chandan's initial profile content."

    def handle(self, *args, **options):
        Experience.objects.filter(company="iEve Era Pvt. Ltd.", role="SEO Specialist").delete()
        Project.objects.filter(name="Search visibility sprint").delete()
        Education.objects.filter(institution="Pt. L R Group of Institutions", qualification="Diploma / Mechanical Engineering").delete()
        Education.objects.filter(institution="Govt Boys Senior Secondary School", qualification="Senior Secondary Education").delete()
        PersonalInformation.objects.update_or_create(pk=1, defaults={
            "name": "Chandan Kumar Paswan",
            "title": "Senior SEO Executive | AI Workflow & Automation Specialist",
            "short_intro": "Senior SEO Executive with 5+ years of experience driving organic growth, keyword rankings, CTR, and conversions through advanced SEO, analytics, performance optimization, and AI-powered workflows.",
            "email": "Paswan.chandan75@gmail.com",
            "phone": "+91 70159 07650",
            "whatsapp_number": "917015907650",
            "location": "Faridabad, India",
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
            "body": "I am Chandan, a Senior SEO Executive with 5+ years of experience in driving organic growth, keyword rankings, CTR, and conversions. I specialize in On-Page, Off-Page, and Technical SEO, analytics, and performance optimization. I also build AI-powered workflows and task-based AI agents to automate SEO operations, reporting, and content processes, with a focus on measurable results across multiple industries.",
            "is_visible": True,
        })
        Experience.objects.filter(company="Singhal Industries Pvt. Ltd.", role="Senior SEO Executive").delete()
        Experience.objects.update_or_create(company="Atomquark Software LLP", role="Senior SEO", defaults={
            "location": "India", "start_date": date(2025, 1, 19), "end_date": None, "is_current": True,
            "responsibilities": "Leading SEO strategy and execution for Atomquark.ai.\nImproving organic visibility through technical SEO, on-page optimization, content strategy, and keyword research.\nMonitoring rankings, traffic, indexing, and performance to drive measurable growth.",
            "tools": "Atomquark.ai, Technical SEO, Keyword research, Google Search Console, Semrush", "sort_order": 1, "is_visible": True,
        })
        Experience.objects.update_or_create(company="iEve Era Pvt. Ltd.", role="SEO Executive", defaults={
            "location": "Mumbai", "start_date": date(2022, 8, 1), "end_date": date(2023, 6, 1),
            "responsibilities": "Implemented SEO strategies resulting in 20% organic traffic growth.\nImproved rankings by 30+ positions for competitive keywords.\nConducted technical SEO audits and applied best practices.\nTracked performance using Google Search Console, Google Analytics, and Semrush.\nCollaborated with content and development teams.",
            "tools": "Semrush, Search Console, Google Analytics, Technical SEO", "sort_order": 2, "is_visible": True,
        })
        Experience.objects.update_or_create(company="AskmeClassified", role="SEO Executive", defaults={
            "location": "Delhi", "start_date": date(2020, 6, 1), "end_date": date(2022, 7, 1),
            "responsibilities": "Executed on-page and off-page SEO strategies.\nPerformed keyword research, competitor analysis, and reporting.\nOptimized website structure and content with internal teams.",
            "tools": "On-page SEO, Off-page SEO, Keyword research, Analytics, Link building", "sort_order": 3, "is_visible": True,
        })
        Experience.objects.update_or_create(company="R V Infotech Pvt. Ltd.", role="SEO Executive", defaults={
            "location": "Faridabad", "start_date": date(2018, 8, 1), "end_date": date(2020, 6, 1),
            "responsibilities": "Implemented SEO best practices for organic growth.\nManaged page optimization, backlink analysis, and reporting.",
            "tools": "On-page SEO, Backlink analysis, Reporting", "sort_order": 4, "is_visible": True,
        })

        skills = [
            ("On-Page SEO", "SEO", "Meta titles, descriptions, internal linking, and content optimization.", 96),
            ("Off-Page SEO", "SEO", "Backlink strategy, authority building, and competitor analysis.", 92),
            ("Technical SEO", "SEO", "Crawlability, indexing, site performance, and technical audits.", 94),
            ("Analytics & reporting", "Analytics", "Google Analytics 4, Search Console, Semrush, and dashboards.", 90),
            ("Google Ads & marketing", "Marketing", "Google Ads, social media, email marketing, and campaigns.", 82),
            ("AI workflow automation", "AI", "Task-based AI agents and automated SEO/content workflows.", 88),
            ("Web development", "Development", "HTML, CSS, JavaScript, WordPress, and conversion-ready UX.", 78),
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
            ("Atomquark.ai", "Web", "SEO and digital growth work for Atomquark Software LLP, focused on building a stronger organic search foundation.", "Technical SEO, Content strategy, Analytics", "Present role / ongoing SEO growth", "https://atomquark.ai"),
            ("Singhal Industries search growth", "SEO", "An organic growth program combining on-page optimization, technical fixes, backlink strategy, and competitor analysis.", "Technical SEO, Semrush, Search Console", "+20% organic traffic / +18% conversions", "https://singhalglobal.com"),
            ("eVe Era SEO program", "SEO", "A multi-domain SEO program focused on technical audits, content collaboration, and competitive keyword growth.", "Technical SEO, Analytics, Reporting", "+30 ranking positions", "https://ieveerafirms.com"),
            ("AskmeClassified SEO", "SEO", "On-page, off-page, keyword research, competitor analysis, and website structure improvements.", "On-page SEO, Link building, Analytics", "Stronger search visibility", "https://askmeclassified.com"),
            ("Nxtwalk digital presence", "Web", "A conversion-focused web presence paired with a search foundation designed to compound.", "WordPress, SEO, UX", "Clearer positioning / stronger organic foundation", "https://www.nxtwalk.in/"),
        ]
        for order, (name, category, description, tools, result, live_url) in enumerate(projects, 1):
            Project.objects.update_or_create(name=name, defaults={"category": category, "description": description, "tools": tools, "result": result, "live_url": live_url, "sort_order": order, "is_visible": True})

        education = [
            ("Pt. L R Group of Institutions", "Diploma in Mechanical Engineering", "Faridabad, Delhi.", 2018),
            ("Govt Boys Senior Secondary School", "12th", "Ballabgarh.", 2016),
            ("Himanshu Memorial School", "10th", "Ballabgarh.", 2014),
        ]
        for order, (institution, qualification, description, end_year) in enumerate(education, 1):
            Education.objects.update_or_create(institution=institution, qualification=qualification, defaults={"description": description, "end_year": end_year, "sort_order": order, "is_visible": True})

        Certification.objects.update_or_create(name="SEO & performance marketing practice", defaults={"issuer": "Professional training", "description": "Applied learning across Google Analytics, Search Console, Semrush, email marketing, and social media strategy.", "sort_order": 1, "is_visible": True})
        Achievement.objects.update_or_create(title="AI-powered SEO workflow automation", defaults={"description": "Built task-based AI workflows and agents to automate SEO operations, reporting, and content processes.", "year": 2026, "sort_order": 1, "is_visible": True})
        Achievement.objects.update_or_create(title="20% organic traffic growth delivered", defaults={"description": "Improved organic traffic through advanced on-page optimization and backlink strategies.", "year": 2023, "sort_order": 2, "is_visible": True})
        SocialLink.objects.update_or_create(platform="LinkedIn", defaults={"label": "LinkedIn", "url": "https://www.linkedin.com/in/seo-chandanpaswan/", "sort_order": 1, "is_visible": True})
        SocialLink.objects.update_or_create(platform="Website", defaults={"label": "Nxtwalk", "url": "https://www.nxtwalk.in/", "sort_order": 2, "is_visible": True})
        SEOSettings.objects.update_or_create(page_key="home", defaults={"title": "Chandan Paswan | Senior SEO Executive & AI Automation Specialist", "meta_description": "Chandan Paswan is a Senior SEO Executive specializing in organic growth, technical SEO, analytics, and AI workflow automation.", "keywords": "Senior SEO Executive, AI workflow automation, technical SEO, organic growth, Chandan Paswan", "canonical_url": "https://www.chandanpaswan.com/"})
        published_at = timezone.make_aware(datetime.combine(date(2026, 9, 12), time.min))
        BlogPost.objects.update_or_create(slug="technical-seo-growth-discipline", defaults={"title": "Why technical SEO is a growth discipline", "excerpt": "Technical work is most valuable when it connects directly to user experience and commercial intent.", "content": "Healthy crawling, clear information architecture, and fast templates make every content investment more discoverable. The best audit is the one that ends with an ordered, owned action list.", "category": "SEO", "tags": "technical SEO, growth, audits", "published_at": published_at, "is_featured": True, "is_published": True})
        self.stdout.write(self.style.SUCCESS("CV content seeded successfully. Upload photos and documents through the admin dashboard."))

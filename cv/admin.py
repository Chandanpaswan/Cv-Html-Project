from django.contrib import admin

from .models import (AboutSection, Achievement, Certification, ContactMessage, Education,
                     Experience, PersonalInformation, Project, SEOSettings, Service, Skill, SocialLink)


class VisibleOrderedAdmin(admin.ModelAdmin):
    list_display = ("__str__", "sort_order", "is_visible", "updated_at")
    list_filter = ("is_visible",)
    list_editable = ("sort_order", "is_visible")
    search_fields = ("__str__",)


@admin.register(PersonalInformation)
class PersonalInformationAdmin(admin.ModelAdmin):
    fieldsets = (("Profile", {"fields": ("name", "title", "short_intro", "profile_photo", "cv_file")}), ("Contact", {"fields": ("email", "phone", "whatsapp_number", "location")}), ("Stats", {"fields": ("years_experience", "traffic_growth", "ranking_improvement", "task_completion")}), ("Visibility", {"fields": ("available_for_work", "is_active")}))


@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    list_display = ("title", "is_visible", "updated_at")


@admin.register(Experience)
class ExperienceAdmin(VisibleOrderedAdmin):
    list_display = ("role", "company", "start_date", "end_date", "sort_order", "is_visible")
    search_fields = ("role", "company", "responsibilities", "tools")


@admin.register(Education)
class EducationAdmin(VisibleOrderedAdmin):
    list_display = ("qualification", "institution", "end_year", "sort_order", "is_visible")
    search_fields = ("qualification", "institution")


@admin.register(Skill)
class SkillAdmin(VisibleOrderedAdmin):
    list_display = ("name", "category", "proficiency", "sort_order", "is_visible")
    list_filter = ("category", "is_visible")
    search_fields = ("name", "description")


@admin.register(Service)
class ServiceAdmin(VisibleOrderedAdmin):
    list_display = ("__str__", "sort_order", "is_visible", "updated_at")
    search_fields = ("name", "description")


@admin.register(Project)
class ProjectAdmin(VisibleOrderedAdmin):
    list_display = ("name", "category", "live_url", "sort_order", "is_visible")
    list_filter = ("category", "is_visible")
    search_fields = ("name", "description", "tools")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Certification)
class CertificationAdmin(VisibleOrderedAdmin):
    list_display = ("name", "issuer", "issued_date", "sort_order", "is_visible")
    search_fields = ("name", "issuer")


@admin.register(Achievement)
class AchievementAdmin(VisibleOrderedAdmin):
    list_display = ("title", "year", "sort_order", "is_visible")
    search_fields = ("title", "description")


@admin.register(SocialLink)
class SocialLinkAdmin(VisibleOrderedAdmin):
    list_display = ("platform", "label", "url", "sort_order", "is_visible")
    search_fields = ("platform", "label", "url")


@admin.register(SEOSettings)
class SEOSettingsAdmin(admin.ModelAdmin):
    list_display = ("page_key", "title", "updated_at")
    search_fields = ("page_key", "title", "meta_description", "keywords")


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_at", "is_read")
    list_filter = ("is_read", "created_at")
    list_editable = ("is_read",)
    search_fields = ("name", "email", "message")
    readonly_fields = ("created_at", "updated_at")

admin.site.site_header = "Chandan Paswan CMS"
admin.site.site_title = "Chandan Paswan CMS"
admin.site.index_title = "Manage your CV website"

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class PersonalInformation(TimeStampedModel):
    name = models.CharField(max_length=120, default="Chandan Kumar Paswan")
    title = models.CharField(max_length=180, default="SEO & Digital Marketing Specialist")
    short_intro = models.TextField(default="I help ambitious businesses become easier to find, trust, and choose.")
    profile_photo = models.ImageField(upload_to="profile/", blank=True)
    cv_file = models.FileField(upload_to="cv/", blank=True)
    email = models.EmailField(default="Paswan.chandan75@gmail.com")
    phone = models.CharField(max_length=30, default="+91 70159 07650")
    whatsapp_number = models.CharField(max_length=30, default="917015907650")
    location = models.CharField(max_length=120, default="India")
    available_for_work = models.BooleanField(default=True)
    years_experience = models.CharField(max_length=20, default="5+")
    traffic_growth = models.CharField(max_length=20, default="20%")
    ranking_improvement = models.CharField(max_length=20, default="30+")
    task_completion = models.CharField(max_length=20, default="98%")
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Personal information"
        verbose_name_plural = "Personal information"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @property
    def whatsapp_url(self):
        return f"https://wa.me/{self.whatsapp_number}?text=Hello%20{slugify(self.name)}%2C%20I%27d%20like%20to%20discuss%20a%20project."


class AboutSection(TimeStampedModel):
    title = models.CharField(max_length=180, default="Curious by nature. Precise by practice.")
    lead = models.TextField(default="I turn search data and business goals into clear, compounding growth.")
    body = models.TextField()
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)


class Experience(TimeStampedModel):
    company = models.CharField(max_length=160)
    role = models.CharField(max_length=160)
    location = models.CharField(max_length=120, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)
    responsibilities = models.TextField(help_text="One responsibility or achievement per line.")
    tools = models.CharField(max_length=500, blank=True, help_text="Comma-separated tools or skills.")
    sort_order = models.PositiveIntegerField(default=0)
    is_visible = models.BooleanField(default=True)

    class Meta:
        ordering = ["-start_date", "sort_order"]

    def __str__(self):
        return f"{self.role} at {self.company}"

    @property
    def responsibility_list(self):
        return [line.strip() for line in self.responsibilities.splitlines() if line.strip()]

    @property
    def tool_list(self):
        return [tool.strip() for tool in self.tools.split(",") if tool.strip()]


class Education(TimeStampedModel):
    institution = models.CharField(max_length=180)
    qualification = models.CharField(max_length=180)
    description = models.TextField(blank=True)
    start_year = models.PositiveIntegerField(null=True, blank=True)
    end_year = models.PositiveIntegerField(null=True, blank=True)
    sort_order = models.PositiveIntegerField(default=0)
    is_visible = models.BooleanField(default=True)

    class Meta:
        ordering = ["sort_order", "-end_year"]

    def __str__(self):
        return f"{self.qualification} - {self.institution}"


class Skill(TimeStampedModel):
    CATEGORY_CHOICES = [(value, value) for value in ("SEO", "Marketing", "Development", "Analytics", "AI")]
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default="SEO")
    description = models.CharField(max_length=220, blank=True)
    proficiency = models.PositiveIntegerField(default=80, validators=[MinValueValidator(1), MaxValueValidator(100)])
    sort_order = models.PositiveIntegerField(default=0)
    is_visible = models.BooleanField(default=True)

    class Meta:
        ordering = ["category", "sort_order", "name"]

    def __str__(self):
        return self.name


class Service(TimeStampedModel):
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=240)
    icon = models.CharField(max_length=40, default="chart")
    sort_order = models.PositiveIntegerField(default=0)
    is_visible = models.BooleanField(default=True)

    class Meta:
        ordering = ["sort_order", "name"]

    def __str__(self):
        return self.name


class Project(TimeStampedModel):
    CATEGORY_CHOICES = [(value, value) for value in ("SEO", "Web", "Marketing")]
    name = models.CharField(max_length=160)
    slug = models.SlugField(max_length=180, unique=True, blank=True)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default="SEO")
    description = models.TextField()
    image = models.ImageField(upload_to="projects/", blank=True)
    tools = models.CharField(max_length=300, blank=True)
    result = models.CharField(max_length=220, blank=True)
    live_url = models.URLField(blank=True)
    case_study_url = models.URLField(blank=True)
    sort_order = models.PositiveIntegerField(default=0)
    is_visible = models.BooleanField(default=True)

    class Meta:
        ordering = ["sort_order", "name"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    @property
    def tool_list(self):
        return [tool.strip() for tool in self.tools.split(",") if tool.strip()]


class Certification(TimeStampedModel):
    name = models.CharField(max_length=180)
    issuer = models.CharField(max_length=160, blank=True)
    issued_date = models.DateField(null=True, blank=True)
    credential_url = models.URLField(blank=True)
    description = models.TextField(blank=True)
    sort_order = models.PositiveIntegerField(default=0)
    is_visible = models.BooleanField(default=True)

    class Meta:
        ordering = ["sort_order", "-issued_date"]

    def __str__(self):
        return self.name


class Achievement(TimeStampedModel):
    title = models.CharField(max_length=180)
    description = models.TextField(blank=True)
    year = models.PositiveIntegerField(null=True, blank=True)
    sort_order = models.PositiveIntegerField(default=0)
    is_visible = models.BooleanField(default=True)

    class Meta:
        ordering = ["sort_order", "-year"]

    def __str__(self):
        return self.title


class SocialLink(TimeStampedModel):
    PLATFORM_CHOICES = [(value, value) for value in ("LinkedIn", "GitHub", "Instagram", "X", "Website")]
    platform = models.CharField(max_length=30, choices=PLATFORM_CHOICES)
    label = models.CharField(max_length=80, blank=True)
    url = models.URLField()
    sort_order = models.PositiveIntegerField(default=0)
    is_visible = models.BooleanField(default=True)

    class Meta:
        ordering = ["sort_order", "platform"]

    def __str__(self):
        return self.label or self.platform


class SEOSettings(TimeStampedModel):
    page_key = models.CharField(max_length=80, unique=True, default="home")
    title = models.CharField(max_length=180)
    meta_description = models.CharField(max_length=320)
    keywords = models.CharField(max_length=500, blank=True)
    canonical_url = models.URLField(blank=True)
    og_image = models.ImageField(upload_to="seo/", blank=True)
    twitter_handle = models.CharField(max_length=80, blank=True)

    def __str__(self):
        return self.page_key


class ContactMessage(TimeStampedModel):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    message = models.TextField()
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.email}"

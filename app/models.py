from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
import uuid

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=50, blank=True)  # For FontAwesome icons
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class TournamentImage(models.Model):
    tournament = models.ForeignKey('Tournament', on_delete=models.CASCADE, related_name='tournament_images')
    image = models.ImageField(upload_to='tournament_images/')
    caption = models.CharField(max_length=200, blank=True)
    is_primary = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.tournament.title}"

class Tournament(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='tournaments')
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organized_tournaments')
    
    # Event Details
    start_date = models.DateField()
    end_date = models.DateField()
    # time = models.TimeField() #default should be 10am
    registration_deadline = models.DateTimeField()
    venue = models.CharField(max_length=200)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    
    # Tournament Specifics
    max_participants = models.PositiveIntegerField()
    min_participants = models.PositiveIntegerField(default=2)
    entry_fee = models.DecimalField(max_digits=10, decimal_places=2)
    prize_pool = models.DecimalField(max_digits=10, decimal_places=2)
    tournament_format = models.CharField(max_length=100)  # e.g., "Single Elimination", "Double Elimination", "Round Robin"
    rules = models.TextField()
    
    # Media
    banner_image = models.ImageField(upload_to='tournament_banners/')
    additional_images = models.ManyToManyField(TournamentImage, blank=True, related_name='additional_tournaments')
    
    # Status and Metadata
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Contact Information
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=20)
    whatsapp_number = models.CharField(max_length=20, blank=True)
    
    # Social Media
    facebook_event = models.URLField(blank=True)
    instagram_post = models.URLField(blank=True)
    
    class Meta:
        ordering = ['-start_date']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Participant(models.Model):
    STATUS_CHOICES = [
        ('registered', 'Registered'),
        ('confirmed', 'Confirmed'),
        ('checked_in', 'Checked In'),
        ('eliminated', 'Eliminated'),
        ('winner', 'Winner'),
        ('disqualified', 'Disqualified'),
        ('rejected', 'Rejected')
    ]

    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='participants')
    registration_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    
    # Personal Information
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    
    # Tournament Specific
    team_name = models.CharField(max_length=100, blank=True)
    player_id = models.CharField(max_length=50, blank=True)  # For gaming tournaments
    rank = models.PositiveIntegerField(null=True, blank=True)
    seed = models.PositiveIntegerField(null=True, blank=True)
    
    # Registration Details
    registration_date = models.DateTimeField(auto_now_add=True)
    payment_status = models.BooleanField(default=False)
    payment_id = models.CharField(max_length=100, blank=True)
    payment_screenshot = models.ImageField(upload_to='tt/', blank=True)
    
    # Status
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='registered')
    check_in_time = models.DateTimeField(null=True, blank=True)
    
    # Additional Information
    emergency_contact = models.CharField(max_length=100)
    emergency_phone = models.CharField(max_length=20)
    special_requirements = models.TextField(blank=True)
    notes = models.TextField(blank=True)

    class Meta:
        unique_together = ['tournament', 'email']

    def __str__(self):
        return f"{self.full_name} - {self.tournament.title}"

class TournamentPrize(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='prizes')
    position = models.PositiveIntegerField()
    prize_amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    winner = models.ForeignKey(Participant, on_delete=models.SET_NULL, null=True, blank=True, related_name='prizes_won')

    class Meta:
        ordering = ['position']
        unique_together = ['tournament', 'position']

    def __str__(self):
        return f"{self.position} Place - {self.tournament.title}"

class TournamentSponsor(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='sponsors')
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='sponsor_logos/')
    website = models.URLField(blank=True)
    sponsorship_level = models.CharField(max_length=50)  # e.g., "Gold", "Silver", "Bronze"
    contribution = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} - {self.tournament.title}"

class TournamentAnnouncement(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='announcements')
    title = models.CharField(max_length=200)
    content = models.TextField()
    is_important = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} - {self.tournament.title}" 
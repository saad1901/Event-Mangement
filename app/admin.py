from django.contrib import admin
from .models import (
    Category, Tournament, TournamentImage, Participant,
    TournamentPrize, TournamentSponsor, TournamentAnnouncement, Upis
)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('created_at', 'updated_at')

class TournamentImageInline(admin.TabularInline):
    model = TournamentImage
    extra = 1
    fields = ('image', 'caption', 'is_primary')

class TournamentPrizeInline(admin.TabularInline):
    model = TournamentPrize
    extra = 1
    fields = ('position', 'prize_amount', 'description', 'winner')

class TournamentSponsorInline(admin.TabularInline):
    model = TournamentSponsor
    extra = 1
    fields = ('name', 'sponsorship_level', 'contribution', 'website')

class TournamentAnnouncementInline(admin.TabularInline):
    model = TournamentAnnouncement
    extra = 1
    fields = ('title', 'content', 'is_important')

@admin.register(Tournament)
class TournamentAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'organizer', 'start_date', 'end_date', 'status', 'is_featured')
    list_filter = ('status', 'category', 'is_featured', 'start_date', 'end_date')
    search_fields = ('title', 'description', 'venue', 'city', 'state')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created_at', 'updated_at')
    inlines = [
        TournamentImageInline,
        TournamentPrizeInline,
        TournamentSponsorInline,
        TournamentAnnouncementInline
    ]
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'description', 'category', 'organizer')
        }),
        ('Event Details', {
            'fields': (
                'start_date', 'end_date', 'registration_deadline',
                'venue', 'address', 'city', 'state', 'country', 'postal_code'
            )
        }),
        ('Tournament Specifics', {
            'fields': (
                'max_participants', 'min_participants', 'entry_fee',
                'prize_pool', 'tournament_format', 'rules'
            )
        }),
        ('Media', {
            'fields': ('banner_image',)
        }),
        ('Status and Metadata', {
            'fields': ('status', 'is_featured', 'created_at', 'updated_at')
        }),
        ('Contact Information', {
            'fields': ('contact_email', 'contact_phone', 'whatsapp_number')
        }),
        ('Social Media', {
            'fields': ('facebook_event', 'instagram_post')
        }),
        ('Payment Information', {
            'fields': ('upi_id',)
        }),
    )

@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'tournament', 'registration_id', 'status', 'registration_date')
    list_filter = ('status', 'registration_date', 'tournament')
    search_fields = ('full_name', 'email', 'phone', 'registration_id')
    readonly_fields = ('registration_id', 'registration_date')
    fieldsets = (
        ('Tournament Information', {
            'fields': ('tournament', 'registration_id', 'registration_date')
        }),
        ('Personal Information', {
            'fields': ('full_name', 'email', 'phone', 'date_of_birth', 'gender')
        }),
        ('Tournament Specific', {
            'fields': ('team_name', 'player_id', 'rank', 'seed')
        }),
        ('Status', {
            'fields': ('status', 'check_in_time')
        }),
        ('Additional Information', {
            'fields': ('emergency_contact', 'emergency_phone', 'special_requirements', 'notes')
        })
    )

@admin.register(TournamentPrize)
class TournamentPrizeAdmin(admin.ModelAdmin):
    list_display = ('tournament', 'position', 'prize_amount', 'winner')
    list_filter = ('tournament', 'position')
    search_fields = ('tournament__title', 'winner__full_name')

@admin.register(TournamentSponsor)
class TournamentSponsorAdmin(admin.ModelAdmin):
    list_display = ('name', 'tournament', 'sponsorship_level', 'contribution')
    list_filter = ('tournament', 'sponsorship_level')
    search_fields = ('name', 'tournament__title')

@admin.register(TournamentAnnouncement)
class TournamentAnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'tournament', 'is_important', 'created_at')
    list_filter = ('tournament', 'is_important', 'created_at')
    search_fields = ('title', 'content', 'tournament__title')
    readonly_fields = ('created_at', 'updated_at') 

admin.site.register(Upis)
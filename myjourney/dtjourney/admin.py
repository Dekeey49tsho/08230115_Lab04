from django.contrib import admin
from .models import LearningJourney, AboutMe

@admin.register(LearningJourney)
class LearningJourneyAdmin(admin.ModelAdmin):
    list_display = ('title', 'description_preview')
    search_fields = ('title', 'description')
    list_per_page = 20
    
    def description_preview(self, obj):
        """Show first 50 characters of description"""
        return obj.description[:50] + '...' if len(obj.description) > 50 else obj.description
    description_preview.short_description = 'Description Preview'

@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ('name', 'bio_preview')
    search_fields = ('name', 'bio')
    list_per_page = 20
    
    def bio_preview(self, obj):
        """Show first 50 characters of bio"""
        return obj.bio[:50] + '...' if len(obj.bio) > 50 else obj.bio
    bio_preview.short_description = 'Bio Preview'

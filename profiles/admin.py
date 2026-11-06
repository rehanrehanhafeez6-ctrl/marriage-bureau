from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'gender', 'city', 'education', 'is_approved', 'created_at')
    list_filter = ('gender', 'city', 'is_approved')
    search_fields = ('full_name', 'city')
    actions = ['approve_profiles']

    @admin.action(description='Selected profiles ko approve karo')
    def approve_profiles(self, request, queryset):
        queryset.update(is_approved=True)
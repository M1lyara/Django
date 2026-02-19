from django.contrib import admin
from .models import Feedback

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'phone', 'created_at')
    search_fields = ('last_name', 'phone')
    list_filter = ('created_at',)
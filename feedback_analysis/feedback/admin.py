from django.contrib import admin
from .models import CustomerFeedback

class CustomerFeedbackAdmin(admin.ModelAdmin):
    list_display = ('review', 'sentiment')  # Columns to display in the list view
    search_fields = ('review',)              # Enable search functionality

admin.site.register(CustomerFeedback, CustomerFeedbackAdmin)



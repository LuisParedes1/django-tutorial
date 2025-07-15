from django.contrib import admin

# Register your models here.
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model=Choice
    extra=3

class QuestionAdmin(admin.ModelAdmin):
    "Columns to display"
    list_display = ["question", "publication_date", "was_published_recently"]
    
    # "Filter” sidebar
    list_filter = ["publication_date"]

    # Number of elements per page. Defaults to 100
    # Admin automatically does pagination
    list_per_page = 20

    # Search by...
    search_fields = ["question"]
    
    # Admin sections
    fieldsets=[
        (None, {"fields": ["question"]}),
        ("Date information", {"fields": ["publication_date"], "classes": ["collapse"]})
    ]

    # Add inline the Choice model
    inlines=[ChoiceInline]

admin.site.register(Question, QuestionAdmin)
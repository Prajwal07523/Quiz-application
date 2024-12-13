from django.contrib import admin
from .models import Question, QuizSession

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'option_a', 'option_b', 'option_c', 'option_d', 'correct_option')  # Display these fields in the list view
    search_fields = ('text',)  # Allow searching by the question text
    list_filter = ('correct_option',)  # Add filtering by the correct option

admin.site.register(Question, QuestionAdmin)
admin.site.register(QuizSession)

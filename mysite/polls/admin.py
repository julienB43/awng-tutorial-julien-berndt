from django.contrib import admin

from .models import Question
from .models import Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0
    
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    
class ChoiceAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Paramètre choix',               {'fields': ['question', 'choice_text']}),
        ('Trucage', {'fields': ['votes']}),
    ]
    list_display = ('choice_text', 'question', 'votes')

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice,ChoiceAdmin)
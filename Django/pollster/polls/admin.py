from django.contrib import admin

# Register your models here.

admin.site.site_header = "Pollster Admin"
admin.site.site_title = "Pollster Admin Area"
admin.site.index_title = "Welcome to Pollster Admin Area"

from .models import Question, Choice

# admin.site.register(Question)
# admin.site.register(Choice)

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields' : ['question_text']}), ('Date Information', {'fields' : ['pub_date'], 'classes':['collapse']}),]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
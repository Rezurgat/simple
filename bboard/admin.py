from django.contrib import admin
from .models import Bb, Rubric

@admin.register(Bb)
class BbAdmin(admin.ModelAdmin):
    list_display = ('title','content','price','published')
    list_display_links= ('title','content')
    search_fields= ('title','content', )

@admin.register(Rubric)
class RubricAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)

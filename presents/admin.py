from django.contrib import admin

# Register your models here.
from .models import Person, Idea


class IdeaInLine(admin.TabularInline):
    model = Idea


class PersonAdmin(admin.ModelAdmin):
    inlines = [IdeaInLine, ]


admin.site.register(Person, PersonAdmin)
admin.site.register(Idea)

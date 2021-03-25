from django.contrib import admin

from .models import Profile, Skills, Experience, Education

class EducationAdmin(admin.ModelAdmin):
    search_fields = ['degree', 'user']
    list_filter = ['degree', 'user']

admin.site.register(Profile)
admin.site.register(Skills)
admin.site.register(Education, EducationAdmin)
admin.site.register(Experience)
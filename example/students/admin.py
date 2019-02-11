from django.contrib import admin

from students.models import Student


class StudentModelaAdmin(admin.ModelAdmin):
    model = Student


admin.site.register(Student, StudentModelaAdmin)

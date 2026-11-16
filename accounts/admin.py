from django.contrib import admin
from .models import StudentProfile


@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):

    list_display = (
        'student_id',
        'user',
        'enrolled_course',
        'section',
    )

    search_fields = (
        'student_id',
        'user__first_name',
        'user__last_name',
    )

    list_filter = (
        'enrolled_course',
        'section',
    )

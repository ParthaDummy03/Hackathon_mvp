from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from accounts.models import StudentProfile


class Command(BaseCommand):

    help = "Create a test student account"

    def handle(self, *args, **kwargs):

        student_id = 'STU001'

        user, user_created = User.objects.get_or_create(
            username=student_id,
            defaults={
                'first_name': 'Rahim',
                'last_name': 'Ahmed',
            }
        )

        if user_created:
            user.set_password('test1234')
            user.save()
            self.stdout.write(self.style.SUCCESS("Student user created."))

        profile, profile_created = StudentProfile.objects.get_or_create(
            user=user,
            defaults={
                'student_id': student_id,
                'enrolled_course': 'BSc in CSE',
                'section': 'A',
            }
        )

        if profile_created:
            self.stdout.write(self.style.SUCCESS("Student profile created."))
        else:
            self.stdout.write(self.style.WARNING("Student profile already exists."))

        if user_created:
            self.stdout.write(
                self.style.SUCCESS("Student ID: STU001 | Password: test1234")
            )

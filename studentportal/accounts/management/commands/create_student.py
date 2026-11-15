from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from accounts.models import StudentProfile


class Command(BaseCommand):
    help = "Create a test student account"

    def handle(self, *args, **kwargs):
        student_id = 'STU001'

        if User.objects.filter(username=student_id).exists():
            self.stdout.write(self.style.WARNING(f"⚠️  User {student_id} already exists."))
            return

        user = User.objects.create_user(
            username=student_id,
            password='test1234',
            first_name='Rahim',
            last_name='Ahmed'
        )
        StudentProfile.objects.create(
            user=user,
            student_id=student_id,
            enrolled_course='BSc in CSE',
            section='A'
        )
        self.stdout.write(self.style.SUCCESS(f"✅ Student '{student_id}' created with password 'test1234'"))
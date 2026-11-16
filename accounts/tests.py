from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import StudentProfile


class StudentPortalTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.student = User.objects.create_user(
            username='STU001', password='test1234',
            first_name='Rahim', last_name='Ahmed',
        )
        StudentProfile.objects.create(
            user=cls.student, student_id='STU001',
            enrolled_course='BSc in CSE', section='A',
        )
        cls.staff = User.objects.create_user(
            username='teacher', password='test1234',
        )

    def test_login_page_loads(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_student_can_login(self):
        response = self.client.post(
            reverse('login'),
            {'username': 'STU001', 'password': 'test1234'},
        )
        self.assertRedirects(response, reverse('dashboard'))

    def test_wrong_password_rejected(self):
        response = self.client.post(
            reverse('login'),
            {'username': 'STU001', 'password': 'wrong'},
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Invalid Student ID or password.')

    def test_user_without_profile_rejected(self):
        response = self.client.post(
            reverse('login'),
            {'username': 'teacher', 'password': 'test1234'},
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No student profile found')

    def test_dashboard_requires_login(self):
        response = self.client.get(reverse('dashboard'))
        self.assertRedirects(
            response, f"{reverse('login')}?next={reverse('dashboard')}"
        )

    def test_dashboard_shows_profile(self):
        self.client.login(username='STU001', password='test1234')
        response = self.client.get(reverse('dashboard'))
        self.assertContains(response, 'Rahim Ahmed')
        self.assertContains(response, 'BSc in CSE')

    def test_logout_requires_post(self):
        self.client.login(username='STU001', password='test1234')
        self.assertEqual(self.client.get(reverse('logout')).status_code, 405)
        response = self.client.post(reverse('logout'))
        self.assertRedirects(response, reverse('login'))

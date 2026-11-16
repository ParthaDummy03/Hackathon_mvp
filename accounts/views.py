from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_POST

from .forms import StudentLoginForm
from .models import StudentProfile


def login_view(request):

    if request.user.is_authenticated:

        if StudentProfile.objects.filter(user=request.user).exists():
            return redirect('dashboard')

        logout(request)
        messages.error(
            request,
            "This account does not have a student profile."
        )

    if request.method == 'POST':

        form = StudentLoginForm(request, data=request.POST)

        if form.is_valid():

            user = form.get_user()

            # Only users with a student profile may sign in
            if StudentProfile.objects.filter(user=user).exists():
                login(request, user)
                return redirect('dashboard')

            messages.error(
                request,
                "No student profile found for this account."
            )

        else:
            messages.error(
                request,
                "Invalid Student ID or password."
            )

    else:
        form = StudentLoginForm()

    return render(request, 'accounts/login.html', {'form': form})


@login_required
def dashboard_view(request):

    profile = StudentProfile.objects.filter(user=request.user).first()

    # Handle users without a student profile
    if profile is None:
        logout(request)
        messages.error(request, "Your student profile was not found.")
        return redirect('login')

    context = {
        'full_name': request.user.get_full_name() or request.user.username,
        'student_id': profile.student_id,
        'course': profile.enrolled_course,
        'section': profile.section,
    }

    return render(request, 'accounts/dashboard.html', context)


@require_POST
def logout_view(request):
    logout(request)
    return redirect('login')

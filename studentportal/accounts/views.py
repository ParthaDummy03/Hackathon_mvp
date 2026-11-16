from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import StudentLoginForm


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = StudentLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, "Invalid Student ID or password.")
        else:
            messages.error(request, "Invalid Student ID or password.")
    else:
        form = StudentLoginForm()

    return render(request, 'accounts/login.html', {'form': form})


@login_required
def dashboard_view(request):
    profile = request.user.profile  # from StudentProfile
    context = {
        'full_name': request.user.get_full_name() or request.user.username,
        'student_id': profile.student_id,
        'course': profile.enrolled_course,
        'section': profile.section,
    }
    return render(request, 'accounts/dashboard.html', context)


def logout_view(request):
    logout(request)
    return redirect('login')
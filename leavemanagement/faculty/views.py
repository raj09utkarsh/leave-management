from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Faculty
from student.models import Application, Student



def FacultyHome(request):
    return render(request, 'faculty/home.html')

def PendingApplications(request):
    user = request.user
    faculty = Faculty.objects.all().filter(user=user).first()
    applications = Application.objects.all().filter(faculty=faculty, is_pending=True)
    context = {
        'applications': applications,
    }

    return render(request, 'faculty/pending.html', context)
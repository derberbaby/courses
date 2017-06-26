from django.shortcuts import render, redirect
from .models import Course

# Create your views here.
def index(request):
    context = {
        "courses": Course.objects.all()
    }
    return render(request, 'course_app/index.html', context)

def add(request):
    Course.objects.create(name=request.POST['name'], description=request.POST['description'])
    courses = Course.objects.all()
    return redirect('/')

def remove(request, id):
    course = Course.objects.get(id=id)
    context = {
        "course": course
    }
    return render(request, 'course_app/remove.html', context)

def no(request):
    return redirect('/')

def yes(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    return redirect('/')

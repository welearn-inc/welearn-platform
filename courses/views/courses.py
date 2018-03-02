from django.forms import formset_factory

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from courses.models import Course
from courses.forms import CourseForm

from accounts.models import Student
from accounts.models import Teacher
import ast

def course_list(request):
    course_list = Course.objects.all()
    paginator = Paginator(course_list, 25) # Show 25 courses per page
    page = request.GET.get('page')
    try:
        courses = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        courses = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        courses = paginator.page(paginator.num_pages)

    return render(request, 'course-list.html',{
        'courses' : course_list,
        'user'    : request.user
    })

def course_detail(request, slug):
    if request.method == "GET":
        course = get_object_or_404(Course, slug=slug)
        # course.goals = ast.literal_eval(course.goals)
        # course.benefits = ast.literal_eval(course.benefits)
    return render(request, 'course-detail.html', {'course': course})

@login_required()
def course_create(request):
    form = CourseForm(request.POST, request.FILES or None)    
    if request.method == "POST":
        if form.is_valid():
            course = form.save(commit=False)
            course.goals = {key:request.POST[key] for key in request.POST if key.split('_')[0] == 'goal'}
            course.benefits = {key:request.POST[key] for key in request.POST if key.split('_')[0] == 'benefit'}
            course.save()
            form.save_m2m() # for tags saving
            return redirect('course-detail', slug=course.slug)
    return render(request, 'course-create.html', {'form': form})

@login_required()
def module_create(request):
    form = CourseForm(request.POST, request.FILES or None)    
    if request.method == "POST":
        if form.is_valid():
            course = form.save(commit=False)
            course.goals = {key:request.POST[key] for key in request.POST if key.split('_')[0] == 'goal'}
            course.benefits = {key:request.POST[key] for key in request.POST if key.split('_')[0] == 'benefit'}
            course.save()
            form.save_m2m() # for tags saving
            return redirect('module-detail', slug=course.slug)
    return render(request, 'module-create.html')

@login_required()
def course_update(request, slug):
    course = get_object_or_404(Course, slug=slug)
    form = CourseForm(instance=course)    
    if request.method == "POST":
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            course = form.save(commit=False)
            course.save()
            form.save_m2m() # for tags saving
            return redirect('course-detail', slug=course.slug)
    return render(request, 'course-update.html', {'form': form})

@login_required()
def course_delete(request, slug):
    course = get_object_or_404(Course, slug=slug)
    # if request.is_ajax():
    Course.objects.get(slug=slug).delete()
    return redirect('course-list')     

@login_required()
def course_enroll(request):
    response_data = {'status' : 'failure', 'message' : 'unsupported request format'}
    if request.is_ajax():
        course_id = int(request.POST['course_id'])
        student = Student.objects.get(user=request.user)
        course = Course.objects.get(id=course_id)

        # Lookup the course in the students enrollment history and if the
        # student is not enrolled, then enroll them now.
        try:
            Course.objects.get(
                students__student_id=student.student_id,
                id=course_id
            )
        except Course.DoesNotExist:
            course.students.add(student)
        response_data = {'status' : 'success', 'message' : 'enrolled' }

    return HttpResponse(json.dumps(response_data), content_type="application/json")
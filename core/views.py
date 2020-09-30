from django.shortcuts import render
from .forms import SignUpForm, CourseForm
from django.views.generic import FormView
from django.http import HttpResponseRedirect, HttpResponse
from .models import Lesson, Course
from django.urls import reverse

# Create your views here.
def register(request):
    template_name = 'registration/register.html'
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('core:login'))
    return render(request, template_name, {'form':form})


class HomeView(FormView):
    template_name = 'core/home.html'
    form_class = CourseForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()

        if form.is_valid():

            course = form.cleaned_data['title']

            form.save()                                                    #will save course title, description and lessons(which are already referenced)

            add_more = form.cleaned_data['add_more'].strip().split(",")    #will convert the more lessons string into list of individual lessons
            crse = Course.objects.get(title=course)
            for i in add_more:
                if Lesson.objects.filter(title=i).exists():                #check if lesson already exists or not
                    lesson = Lesson.objects.get(title=i)
                    crse.lessons.add(lesson)                                #if exists add the relationship of the lesson with the course object saved above.
                else:
                    lesson = Lesson(title=i)                                #if not save the added lessons and then make a relation with the course object saved above.
                    lesson.save()
                    crse.lessons.add(lesson)

            return HttpResponse("saved Successfully")

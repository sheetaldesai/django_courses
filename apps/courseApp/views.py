# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Courses, Description
from .forms import CourseForm
from django.utils import timezone


def index (request) :
    # context = {'users': Users.objects.all()
    form = CourseForm()
    courses = Courses.objects.all()
    print "courses: ",courses
    context = {"courses":[], "form": form}
    for course in courses :
        print "course: ", course
        try :
            desc = Description.objects.get(course_name=course)
        except Description.DoesNotExist:
            desc = None
        context["courses"].append({"id":course.id,"name": course.name,"desc":desc})
        print "context: ", context
       
    print context

    return render(request, 'courseApp/index.html',context)

def add (request) :
    if request.method == "POST":
        courese = Courses(name=request.POST['name'])
        courese.save()
    
    if "desc" in request.POST :
        Description.objects.create(course_name = courese, desc=request.POST["desc"])

    return redirect(reverse('courses:home'))

def remove(request, id) :
    course = Courses.objects.get(pk=id)
    try :
        desc = Description.objects.get(course_name=course)
        desc1 = desc.desc
    except Description.DoesNotExist:
        desc1 = None
    context = {
        "name": course.name,
        "desc": desc1,
        "id": id
    }
    return render(request, 'courseApp/remove.html',context)    

def removeConfirm(request,id) :
    courese = Courses.objects.get(pk=id)
    courese.delete()
    return redirect(reverse('courses:home'))
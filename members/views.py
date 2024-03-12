from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def members(request):
    return HttpResponse("Hello world!")
def my_first(request):
  template = loader.get_template('my_first.html')
  return HttpResponse(template.render())
def home_views(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())
def completed_views(request):
  template = loader.get_template('completed.html')
  return HttpResponse(template.render())
def remaining_views(request):
  template = loader.get_template('remaining.html')
  return HttpResponse(template.render())
def add_task_views(request):
  template = loader.get_template('add_task.html')
  return HttpResponse(template.render())
def delete_views(request):
  template = loader.get_template('delete.html')
  return HttpResponse(template.render())
def task_views(request):
  template = loader.get_template('task_details.html')
  return HttpResponse(template.render())
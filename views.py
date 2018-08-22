# coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime


def sayHello(request):
    s = 'Hello World!'
    current_time = datetime.datetime.now()
    html = '<html><head></head><body><h1> %s </h1><p> %s </p></body></html>' % (s, current_time)
    return HttpResponse(html)

def showStudents(request):
    list = [{id: 1, 'name': 'Jack', 'age': '24', 'sex': '男'}, {id: 2, 'name': 'Rose', 'age': '26', 'sex': '女'}]
    return render_to_response('student.html',{'students': list})
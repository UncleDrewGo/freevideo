from django.shortcuts import render

# Create your views here.
from videoapp.models import people
from django.template import Context, Template
from django.shortcuts import render, HttpResponse


def firstView(request):
    p1 = people(name='wj', job='developer')
    html_string ='''
       fgfdg {{ p1.name }}
        '''

    t = Template(html_string)
    c = Context({"p1": p1})

    web_page = t.render(c)
    return HttpResponse(web_page)

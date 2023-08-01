from django.http import HttpResponse
from articels.models import Articels
from django.template.loader import render_to_string,get_template

def say_hello(request,*args,**kwargs):
    obj=Articels.objects.all()
    context={
        "objects":obj,

    }

    html=render_to_string("home_view.html",context=context)
    return HttpResponse(html)
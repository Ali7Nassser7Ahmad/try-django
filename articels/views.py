from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Articels
from .forms import ArticleForm
# Create your views here.

@login_required()
def article_create_view(request):
    form=ArticleForm(request.POST or None)
    context = {"form":form}
    if form.is_valid():
        obj=form.save()
        form=ArticleForm()
        context["form"] = form
        context["article_create"] = True
        context["object"]=obj
    return render(request,"articles/create.html",context=context)

def article_search_view(request):

    query_dict=request.GET # this is a dictionary

    obj=None
    try:
        query = int(query_dict.get("q"))  # <input type="text" name="q"/>
    except:
        query=None
    if query is not None:
        obj=Articels.objects.get(id=query)

    context={"obj_details":obj}
    return render(request,"articles/search.html",context=context)


def article_detail_view(request,id,*args,**kwargs):
    obj=Articels.objects.get(id=id)
    context={
        'obj_details':obj,
    }

    return render(request,"articles/detail.html",context=context)
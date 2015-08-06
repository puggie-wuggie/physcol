from django.shortcuts import render
from django.template import RequestContext, loader
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.models import User


def login(request):
    user_list = User.objects.all()
    template = loader.get_template('phys/index.html')
    context = RequestContext(request, {'user_list':user_list })
    return HttpResponse(template.render(context))

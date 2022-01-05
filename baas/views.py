from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
# Create your views here.



def index(request):
    latest_question_list = ['sadasds']
    # template = loader.get_template('baas/index.html')
    template = loader.get_template('quote-and-buy.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
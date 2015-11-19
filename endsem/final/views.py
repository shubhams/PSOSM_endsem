from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

# Create your views here.
def index(request):
	template = loader.get_template('final/index.html')
	msg="The end is nigh..."
	context = RequestContext(request, {
		'welcome_msg': msg,
		})
	return HttpResponse(template.render(context))

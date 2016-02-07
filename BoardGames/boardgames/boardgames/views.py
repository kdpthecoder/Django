#from django.views.generic.base import View
#from django.http import HttpResponse

from datetime import date
#from django.shortcuts import render_to_response

from django.views.generic.base import TemplateView

#class HelloWorldView(View):
#	def get(self, request):
#		return HttpResponse("Hello World!!!")

#class HelloWorldView(View):
#        def get(self, request):
#                return render_to_response('HelloWorld.html',{'date':date.today()} )

class HelloWorldView(TemplateView):
	template_name="HelloWorld.html"

	def get_context_data(self, **kwargs):
		return {'date': date.today()}


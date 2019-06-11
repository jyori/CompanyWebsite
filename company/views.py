from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .models import top3post, partner, totalpost
# Create your views here.
def index(request):
	context= {
	 "allcontent":top3post.objects.all(),
	 "sponsors": partner.objects.all()
	}
	return render(request,'company/index.html', context)

def about(request):
	return render(request,'company/about.html')

def E_commerce(request):
	return render(request,'company/E_commerce.html')

def elements(request):
	return render(request,'company/elements.html')

def erp_development(request):
	return render(request,'company/erp_development.html')

def Graphic_design(request):
	return render(request,'company/Graphic_design.html')

def internet_marketing(request):
	return render(request,'company/internet_marketing.html')

def mobile_app_development(request):
	return render(request,'company/mobile_app_development.html')

def multivendor(request):
	return render(request,'company/multivendor.html')

def open_source_development(request):
	return render(request,'company/open_source_development.html')

def services(request):
	return render(request,'company/services.html')

def software_solutions(request):
	return render(request,'company/software_solutions.html')

def traning(request):
	return render(request,'company/traning.html')

def web_application(request):
	return render(request,'company/web_application.html')

def web_development(request):
	return render(request,'company/web_development.html')

def web_hosting(request):
	return render(request,'company/web_hosting.html')
def projects(request):
	return render(request,'company/projects.html')
def career(request):
	context= {
	 "content":totalpost.objects.all(),
	}
	return render(request,'company/career.html', context)
def contact(request):
	form 
	return render(request,'company/contact.html')
#def thanksmail(request):

from django.shortcuts import render
from django.http import HttpResponse
from django.templatetags.static import static
from .licence_stats import generate_licence_stats
from .users_data import generate_user_data
from django.http import JsonResponse

# Create your views here.

def home_view(request):
	return render(request, "home.html", {})
def welcome(request):
	return render(request, "welcome.html", {})
def stats(request):
	data = generate_licence_stats()
	return render(request, "stats.html", {'no_of_line': data })
def user_stats(request):
	data =  generate_user_data()
	return render(request, "user_stats.html" ,{'user_data' : data})
def lmt_admin(request):
	default_data={
	"tc_root" : "/users/xyz/root",
	"tc_data" : "/users/xyz/root/tc_data.log",
	"pwd" : "/users",
	"logfile_root" : "/users/xyz/root/logfile.log",
	"admin_username" : "Omnium Consultants",
	"admin_pass" : "ABCD@1234",

	}
	return render(request, "lmt_admin.html" ,default_data)
def save_changes(request):
	tc_root=request.POST.get('tc_root', None)
	tc_data=request.POST.get('tc_data', None)
	pwd=request.POST.get('pwd', None)
	logfile_root=request.POST.get('logfile_root', None)
	admin_username=request.POST.get('admin_username', None)
	admin_pass=request.POST.get('admin_pass', None)

	data={'saved': 'sucessfuly'}
	# do whatever with the variables
	return JsonResponse(data)
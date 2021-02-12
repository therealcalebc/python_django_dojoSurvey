from django.shortcuts import render, redirect

# Create your views here.
def index(request):
	context = {
		"title": "Dojo Survey"
	}
	return render(request, "index.html", context)

def result(request):
	print(request.POST)
	if 'favorite' in request.POST:
		fav = request.POST['favorite']
	else:
		fav = "Not Specified"
	if 'robot' in request.POST:
		robot = 'You Are Not A Robot'
	else:
		robot = 'You Are A Robot'
	context = {
		"title": "Dojo Survey",
		"name_from_form": request.POST['name'],
		"email_from_form": request.POST['email'],
		"location_from_form": request.POST['location'],
		"favLang_from_form": fav,
		"comments_from_form": request.POST['comments'],
		"robot_from_form": robot
	}
	return render(request, "success.html", context)

def back(request):
	return redirect("/")
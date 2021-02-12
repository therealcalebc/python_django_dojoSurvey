from django.shortcuts import render, redirect

# Create your views here.
def index(request):
	context = {
		"title": "Dojo Survey"
	}
	return render(request, "index.html", context)

def result(request):
	print(request.POST)
	context = {
		"title": "Dojo Survey",
		"name_from_form": request.POST['name'],
		"email_from_form": request.POST['email'],
		"location_from_form": request.POST['location'],
		"favLang_from_form": request.POST['favorite'],
		"comments_from_form": request.POST['comments'],
	}
	return render(request, "success.html", context)

def back(request):
	return redirect("/")
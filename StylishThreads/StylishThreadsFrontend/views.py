from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    if request.method == "GET":
        return render(request, "home.html")
    if request.method == "POST":
        user_id = request.POST.get('user_id')
        name = request.POST.get('name')
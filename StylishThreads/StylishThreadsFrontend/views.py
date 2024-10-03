from django.shortcuts import render, HttpResponse
import pandas as pd
from django.template.loader import render_to_string
from StylishThreads.static import generated_emails1

# Create your views here.
def index(request):
    if request.method == "GET":
        print('post')
        user_id = request.POST.get('user_id')
        name = request.POST.get('name')
        df = pd.read_csv(generated_emails1)
        email = df[df['user_id'] == int(user_id)]['email'].values[0]
        return render(request, "output.html", email=email)
        # return render(request, "home.html")
    if request.method == "POST":
        print('post')
        user_id = request.POST.get('user_id')
        name = request.POST.get('name')
        df = pd.read_csv('StylishThreads/static/generated_emails1.csv')
        email = df[df['user_id'] == int(user_id)]['email'].values[0]
        return render(request, "output.html", email=email)
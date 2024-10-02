from django.shortcuts import render, HttpResponse
import pandas as pd
from django.template.loader import render_to_string

# Create your views here.
def index(request):
    if request.method == "GET":
        return render(request, "home.html")
    if request.method == "POST":
        print('post')
        user_id = request.POST.get('user_id')
        name = request.POST.get('name')
        df = pd.read_csv('../static/generated_emails1.csv')
        email = df[df['user_id'] == int(user_id)]['email'].values[0]
        return render(request, "output.html", email=email)
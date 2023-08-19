from django.shortcuts import render
from django.contrib.auth.decorators import login_required


#@login_required(login_url = '/login/')
def home_view(request):
    context  = dict()

    return render(request,"core/index.html", context)



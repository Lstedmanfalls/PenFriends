from django.shortcuts import render

from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from login_registration_app.models import User

def penfriends(request): #GET REQUEST
    if "user_id" not in request.session:
        messages.error(request, "You must be logged in to view this site")
        return redirect ("/")
    else:
        context = {
        "this_user": User.objects.get(id=request.session["user_id"]),
    }
    return render(request, "penfriends.html", context)
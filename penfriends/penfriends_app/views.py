from penfriends.penfriends_app.models import Message
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

    # mark's views

def inbox(request):
    if "user_id" not in request.session:
        messages.error(request, "You must be logged in to view this site")
        return redirect ("/")
    else:
        context = {
            "this_user": User.objects.get(id = request.session["user_id"]),
            "user_messages" : Message.objects.filter(recipient = request.session["user_id"]),
        }
        return render (request, "inbox.html", context)

def message(request, message_id):
    if "user_id" not in request.session:
        messages.error(request, "You must be logged in to view this site")
        return redirect ("/")
    else:
        context = { 
            "this_user": User.objects.get(id = request.session["user_id"]),
            "this_message" : Message.objects.get(id = message_id)
        }
        return render (request, "message.html", context)

def mark_read(request, message_id):
    this_message = Message.objects.get(id = message_id)
    this_message.unread = False
    this_message.save()
    return redirect("/inbox")

    # end mark's views
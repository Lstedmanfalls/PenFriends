
from django.shortcuts import render
from .models import Resident,Message,Post
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
def new_message(reqeust):
    pass

#julie's views
def userdash(request,user_id):
    if "user_id" not in request.session:
        messages.error(request, "You must be logged in to view this site")
        return redirect ("/")
    else:
        context={
            "this_user":User.objects.get(id = request.session["user_id"])
        }
        return render(request,'admindash.html',context)

def createresident(request,user_id):
    if "user_id" not in request.session:
        messages.error(request, "You must be logged in to view this site")
        return redirect ("/")
    
    else:
        this_user=User.objects.get(id=request.session['user_id'])
        if request.method=="POST" and this_user.category=="admin":
            Resident.objects.create(
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                picture = request.FILES['picture'],
                bio = request.POST['bio'],
                creator=this_user
                )
        return redirect(f'/penfriends/dashboard/{user_id}')
def createpost(request,user_id):
    if "user_id" not in request.session:
        messages.error(request, "You must be logged in to view this site")
        return redirect ("/")
    else:
        user=User.objects.get(id=request.session['user_id'])
        recipient=Resident.objects.get(id=request.POST['for_resident'])
        if request.method=="POST" and user.category=="admin":  

            Post.objects.create(
                title=request.POST['title'],
                body=request.POST['body'],
                maker=user,
                for_resident=recipient
            )
        return redirect(f'/penfriends/dashboard/{user_id}')
def updatepost(request,user_id,post_id):
    if "user_id" not in request.session:
        messages.error(request, "You must be logged in to view this site")
        return redirect ("/")
    else:
        update_post=Post.objects.get(id=post_id)
        if request.method=="POST":
            update_post.title=request.POST['title']
            update_post.body=request.POST['body']
            update_post.save()
        
        return redirect(f'/penfriends/dashboard/{user_id}')  
def deletepost(request,user_id,post_id):
    if "user_id" not in request.session:
        messages.error(request, "You must be logged in to view this site")
        return redirect ("/")
    else:
        if request.method=="POST":
            this_post=Post.objects.get(id=post_id)
            this_post.delete()
            return redirect(f'/penfriends/dashboard/{user_id}')
def residentprofile(request,resident_id):
    if "user_id" not in request.session:
        messages.error(request, "You must be logged in to view this site")
        return redirect ("/")
    else:
        context={
            "this_resident":Resident.objects.get(id=resident_id),
            "this_user":User.objects.get(id=request.session['user_id'])
        }
        return render(request,"residentprofile.html",context)
def updateresident(request,resident_id):
    if "user_id" not in request.session:
        messages.error(request, "You must be logged in to view this site")
        return redirect ("/")
    else:
        update_resident=Resident.objects.get(id=resident_id)
        if request.method=="POST":
            update_resident.first_name=request.POST['first_name']
            update_resident.last_name=request.POST['last_name']
            update_resident.bio=request.POST['bio']
            update_resident.picture=request.FILES['picture']
            update_resident.save()
        messages.success(request,"Resident info updated successfully!")
        return redirect(f'/penfriends/resident/{resident_id}')   

def deleteresident(request,resident_id,user_id):
    if "user_id" not in request.session:
        messages.error(request, "You must be logged in to view this site")
        return redirect ("/")
    else:
        if request.method=="POST":
            this_resident=Resident.objects.get(id=resident_id)
            this_resident.delete()
            return redirect(f'/penfriends/dashboard/{user_id}')

def new_messagepage(request):
    if "user_id" not in request.session:
        messages.error(request, "You must be logged in to view this site")
        return redirect ("/")
    else:
        context={
            
            "this_user":User.objects.get(id=request.session['user_id'])
        }
        return render(request,"newmsgpage.html",context)
def createmessage(request):
    if "user_id" not in request.session:
        messages.error(request, "You must be logged in to view this site")
        return redirect ("/")
    else:
        user=User.objects.get(id=request.session['user_id'])
        this_resident=Resident.objects.get(id=request.POST['recipient'])
        if request.method=="POST" and user.category=="penpal":
            Message.objects.create(
                subject = request.POST['subject'],
                content = request.POST['content'],
                attachment = request.FILES['attachment'],
                creator = user,
                recipient=this_resident
                
            )
        return redirect('/penfriends/message/new_message')
    
#end julie's views
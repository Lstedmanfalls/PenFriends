from django.urls import path
from . import views

urlpatterns = [
    path('', views.penfriends), #GET request to display home page
    
    # mark's urls - need to add beginning slash to all urls (root is penfriends links)
    
    path('/inbox', views.inbox),
    path('/inbox/', views.inbox),
    path('/message/compose', views.new_message),
    path('/message/compose/', views.new_message),
    path('/message/<int:message_id>', views.message),
    path('/message/<int:message_id>/', views.message),
    path('/message/<int:message_id>/mark_read', views.mark_read),

    # end mark's urls 
    
    #julie's urls
    path('/dashboard/<int:user_id>',views.userdash),
    path('/dashboard/<int:user_id>/createresident',views.createresident),
    path('/dashboard/<int:user_id>/createpost',views.createpost),
    path('/resident/<int:user_id>/<int:post_id>/updatepost',views.updatepost),
    path('/resident/<int:user_id>/<int:post_id>/deletepost',views.deletepost),
    path('/resident/<int:resident_id>',views.residentprofile),
    path('/resident/<int:resident_id>/updateresident',views.updateresident),
    path('/resident/<int:resident_id>/<int:user_id>/delete',views.deleteresident),
    path('/message/new_message',views.new_messagepage),
    path('/message/new_message/create',views.createmessage),
    #end julie's urls
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.penfriends), #GET request to display home page
    
    # mark's urls 
    
    path('inbox', views.inbox),
    path('inbox/', views.inbox),
    path('message/compose', views.new_message),
    path('message/compose/', views.new_message),
    path('message/<int:message_id>', views.message),
    path('message/<int:message_id>/', views.message),
    path('message/<int:message_id>/mark_read', views.mark_read),

    # end mark's urls 
]
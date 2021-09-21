from django.urls import path
from . import views

urlpatterns = [
    # Seeking PenFriends Page (Home)
    path('', views.penfriends),
    path('/become_penfriend', views.become_penfriend),

    # Admin Dashboard Page   
    path('/dashboard/admin', views.admindash),
    path('/dashboard/admin/createresident', views.createresident),
    path('/dashboard/admin/createpost', views.createpost),
    path('/resident/<int:post_id>/updatepost', views.updatepost),
    path('/resident/<int:post_id>/deletepost', views.deletepost),

    # Penpal Dashboard Page
    path('/dashboard/penpal', views.penpal_dash),
    path('/dashboard/penpal/update_password', views.update_penpal_password),

    # Resident Profile Page
    path('/resident/<int:resident_id>', views.residentprofile),
    path('/resident/<int:resident_id>/updateresident', views.updateresident),
    path('/resident/<int:resident_id>/delete', views.deleteresident),

    # Inbox Page
    path('/inbox', views.inbox),
    path('/message/<int:message_id>/mark_read', views.mark_read),

    # Create Message Page
    path('/message/new_message', views.new_message),
    path('/message/create_message', views.create_message),

    # View Message Page
    path('/message/<int:message_id>', views.message),
]
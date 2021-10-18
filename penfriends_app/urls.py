from django.urls import path
from . import views

urlpatterns = [
    # Seeking PenFriends Page (Home)
    path('', views.home),
    path('/become_penfriend', views.become_penfriend),

    # Admin Dashboard Page   
    path('/dashboard/admin', views.dash_admin),
    path('/dashboard/admin/createresident', views.create_resident),
    path('/dashboard/admin/createpost', views.create_post),
    path('/resident/<int:post_id>/updatepost', views.update_post),
    path('/resident/<int:post_id>/deletepost', views.delete_post),

    # Penpal Dashboard Page
    path('/dashboard/penpal', views.dash_penfriend),
    path('/dashboard/penpal/update_password', views.update_penfriend_password),
    path('/dashboard/penpal/remove_penpal', views.remove_penfriend),

    # Resident Profile Page
    path('/resident/<int:resident_id>', views.resident_profile),
    path('/resident/<int:resident_id>/updateresident', views.update_resident),
    path('/resident/<int:resident_id>/delete', views.delete_resident),

    # Inbox Page
    path('/inbox', views.inbox),
    path('/message/mark_read', views.mark_read),
    path('/message/mark_unread', views.mark_unread),

    # Sent Message Page
    path('/sent', views.sent),

    # Create Message Page
    path('/message/new_message', views.new_message),
    path('/message/create_message', views.create_message),

    # View Message Page
    path('/message/<int:message_id>', views.message),
]

from django.urls import path
from blogapp import views

urlpatterns = [
    path('home/',views.home_view),
    path("register/",views.user_register_view),
    path("list/",views.list_of_blogs),
    path("add/",views.add_new_blog_view),
    path("detail/<int:id>/",views.detail_view),
    path("update/<int:id>/",views.blog_update_view),
    path("delete/<int:id>/",views.blog_delete_view),
    
]

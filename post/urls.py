from django.urls import path, include
from .views import Postdetails, Createpost, Deletepost, Updatepost
urlpatterns = [
    path("postdetails/<int:pk>/", Postdetails.as_view(), name='postdetails'),
    path("createpost/", Createpost.as_view(), name='createpost'),
    path("deletpost/<int:pk>", Deletepost.as_view(), name='deletepost'),
    path("updatepost/<int:pk>", Updatepost.as_view(), name='updatepost'),
]
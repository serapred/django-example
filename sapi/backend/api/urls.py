from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenBlacklistView
from . import views

urlpatterns = [
    path("notes/", views.NoteListCreateView.as_view(), name="list-note"),
    path("notes/delete/<int:pk>", views.NoteDeleteView.as_view(), name="delete-note"),
    path("user/register/", views.CreateUserView.as_view(), name="register"),
    path("user/profile/", views.ProfileUserView.as_view(), name="profile"),
    path("user/token/", TokenObtainPairView.as_view(), name="get-token"),
    path("user/token/refresh/", TokenRefreshView.as_view(), name="refresh-token"),
    path("user/token/blacklist/", TokenBlacklistView.as_view(), name="blacklist-token"),
    path("user/auth/", include("rest_framework.urls")),
]
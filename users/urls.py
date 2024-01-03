"""Users URLs."""

# Django

from django.urls import path

# Views

from users import views

urlpatterns = [

    # Management
    path(
        route='users/login/',
        view=views.LoginView.as_view(),
        name='login'
    ),

    path(
        route='users/logout/',
        view=views.logout_view,
        name='logout'
    ),

    path(
        route='users/signup/',
        view=views.SignupView.as_view(),
        name='signup'
    ),

    path(
        route='users/me/profile/',
        view=views.UpdateProfileView.as_view(),
        name='update'
    ),

    # Posts
    path(
        route='users/<str:username>/',
        view=views.UserDetailView.as_view(),
        name='detail'
    )
]

"""litreview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

import authentication.views
import review.views

from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView)

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    ####
    # Bloc authentication
    path('', LoginView.as_view(
        template_name='authentication/login.html',
        redirect_authenticated_user=True
    ), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', authentication.views.Signup.as_view(), name='signup'),
    path('password-change/', PasswordChangeView.as_view(
        template_name='authentication/password_change.html'
        ), name='password-change'),
    path('password-change-done/', PasswordChangeDoneView.as_view(
        template_name='authentication/password_change_done.html'
        ), name='password_change_done'),
    path(
        'search-users/<str:follow_unfollow>/<int:user_id>/',
        authentication.views.FollowUser.as_view(),
        name='follow-user'
    ),
    path(
        'profil-pic-change/',
        authentication.views.ProfilPicChange.as_view(),
        name='profile-picture-change'
    ),
    ####
    # Bloc tickets and reveiws
    path(
        'ticket/create/',
        review.views.TicketCreate.as_view(), name='ticket-create'),
    path(
        'ticket/modify/<int:ticket_id>/',
        review.views.TicketModify.as_view(), name='ticket-modify'),
    path(
        'review/<int:ticket_id>/create/',
        review.views.ReviewCreate.as_view(), name='review-create'),
    path(
        'review/modify/<int:review_id>/',
        review.views.ReviewModify.as_view(), name='review-modify'),
    path(
        'review/ticket/create/',
        review.views.ReviewAndTicketCreate.as_view(),
        name='review-ticket-create'),
    ####
    # Bloc flux
    path('flux/', review.views.Flux.as_view(), name='flux'),
    path('flux/self/', review.views.FluxSelf.as_view(), name='flux-self'),
    path('flux/perso/', review.views.FluxPerso.as_view(), name='flux-perso'),
    path(
        'flux/user/<int:user_id>/',
        review.views.FluxUser.as_view(), name='flux-user'),
    path(
        'flux/user/<int:user_id>/follow/',
        review.views.FluxUser.as_view(), name='flux-user-follow'),
    path(
        'flux/user/<int:user_id>/unfollow/',
        review.views.FluxUser.as_view(), name='flux-user-unfollow'),
    path(
        'flux/<str:author_name>/<str:book_title>/',
        review.views.FluxBook.as_view(), name='flux-book'),
    path(
        'flux-ticket/<int:ticket_id>/',
        review.views.FluxTicket.as_view(), name='flux-ticket')
    ####
]

# DEBUG = True means that I am in a dev environement
# Add the media urls to the urlpatterns
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )

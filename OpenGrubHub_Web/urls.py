"""rnd_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include


urlpatterns = [
    # path('',home_view,name="home"),
    path("admin/", admin.site.urls),
    path("", include("EntryPage.urls")),
    path("profiles/", include("Profiles.urls")),
    path("upload/", include("FileUpload.urls")),
    path("reservation/", include("ReservationApp.urls")),
    path("restaurant-find/", include("RestaurantFinder.urls")),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),
]

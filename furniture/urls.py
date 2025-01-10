"""
URL configuration for furniture project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from furniture_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('about/',views.about,name='abouts'),
    path('contact/',views.contacts,name='contacts'),
    path('404/',views.error,name='error'),
    path('service/',views.services,name='service'),
    path('project/',views.projects,name='project'),
    path('feature/',views.features,name='feature'),
    path('quote/',views.quotes,name='quote'),
    path('team/',views.teams,name='team'),
    path('testimonial/',views.testimonials,name='testimonial'),
    path('booking/',views.booking,name='bookings'),

    path('login/',views.login_view,name='login'),
    path('sign-up/',views.sign_up,name='sign_up'),
    path('logout/',views.logout_view,name='logout'),



]

"""uid_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from add_upd import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('captcha/',views.getCaptcha),
    path('otp',views.getOTP),
    path('signup',views.SignUp),
    path('login',views.Login),
    path('request-address',views.requestForSharingAddress),
    # path('accept',views.ResponseToRequestForAddress)
]

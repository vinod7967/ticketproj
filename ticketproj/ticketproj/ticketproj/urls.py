"""ticketproj URL Configuration

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
from ticketapp import views 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.user_login,name='login'),
    path('signup',views.signup,name='signup'),
    path('ticket',views.ticket_rise,name='ticket'),
    #path('delete/<int:id>',views.delete,name='delete'),
    #path('update/<int:id>',views.update,name='update'),
    #path('success/',views.success,name='success'),
    path('logout/',views.user_logout,name='logout'),
    path('adminpage',views.adminpage,name='admin'),
    path('update/<int:id>', views.update, name='update'),
]

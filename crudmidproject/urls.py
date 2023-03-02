"""crudmidproject URL Configuration

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
from django.urls import path
from crudmidproject import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='my-home'),
    path('insert',views.insertData,name='my-insert'),
    path('login',views.handlelogin,name='my-login'),
    path('logout',views.handlelogout,name='my=logout'),
    path('signup',views.handlesignup,name='my-signup'),
    path('update/<id>',views.updateData,name='updateData'),
    path('delete/<id>',views.deleteData,name='deletedata')
]

"""project10 URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from myapp import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('admin_login/',views.admin_login,name='admin_login'),
    path('normal_user/',views.normal_user,name='normal_user'),
    path('normal_login/',views.normal_login,name='normal_login'),
    path('dash/',views.dash,name='dash'),
    path('normal_logout/',views.normal_logout,name='normal_logout'),
    path('login_user/',views.login_user,name='login_user'),
    path('index/', LogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout_user/',views.logout_user,name='logout_user'),
    path('regs/',views.regs,name='regs'),
    path('create_user/',views.create_user,name='create_user'),
    path('example/',views.example,name='example'),
    path('profile/',views.profile,name='profile'),
    path('add_address/',views.add_address,name='add_address'),
    path('save_address/',views.save_address,name='save_address'),
    path('add_to_cart/<int:id>/',views.add_to_cart,name='add_to_cart'),
    path('cart/',views.cart,name='cart'),
    path('clear_cart/',views.clear_cart,name='clear_cart'),
    path('checkout/',views.checkout,name='checkout'),
    path('payment/',views.payment,name='payment'),
    path('order/',views.order,name='order'),

    path('contact/',views.contact,name='contact'),
    path('order_status/<int:id>/',views.order_status,name='order_status'),
    path('order_new/',views.order_new,name='order_new'),

    path('sendmail/', views.sendmail, name='sendmail'),
    path('check/', views.check, name='check'),
    path('email/',views.email,name='email'),





]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
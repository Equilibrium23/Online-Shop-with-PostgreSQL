"""Online_Shop URL Configuration

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
from django.urls import path, register_converter
from register_and_login import views as register_and_login_views 
from user_profile import views as user_profile_views 
from search_and_filter import views as searching_views 
from administration import views as administration_views 
from home import views as home_views


urlpatterns = [
    path('', home_views.home, name = "home"),
    path('admin/', admin.site.urls),
    path('admin_home/', administration_views.home, name = "admin_home"),
    path('admin_home/logout/', administration_views.logout, name = "adm_logout"),
    path('admin_home/manage/', administration_views.manage, name = "manage"),
    path('login/', register_and_login_views.login,name = "login"),
    path('register/', register_and_login_views.register,name = "register"),
    path('logged/', user_profile_views.logged,name = "logged"),
    path('logged/basket/', user_profile_views.basket,name = "basket"),
    path('logged/basket/order/', user_profile_views.make_order,name = "order"),
    path('logged/search/', searching_views .search_items,name = "search"),
    path('logged/search/filter/', searching_views.filter_items,name = "search_filter"),
    path('logged/profile/', user_profile_views.profile,name = "profile"),
    path('logged/profile/logout/', user_profile_views.logout,name = "logout"),
    path('logged/profile/orders', user_profile_views.user_orders,name = "orders"),
    path('logged/profile/return/', user_profile_views.return_product,name = "return"),
    path('logged/profile/returns/', user_profile_views.show_return_products,name = "returns"),
    path('logged/profile/opinions/', user_profile_views.user_opinions,name = "opinions"),
    path('logged/profile/opinion/', user_profile_views.add_opinion,name = "opinion"),
    path('logged/profile/account_details/', user_profile_views.account_details,name = "account_details"),
    path('logged/profile/account_details/adress/', user_profile_views.set_main_adress,name = "adress"),
    path('logged/profile/account_details/adress/delete/', user_profile_views.delete_user_adress,name = "delete"),
    path('logged/basket/<int:monitor_id>/', user_profile_views.add_item_to_basket,name = "basket"),
]

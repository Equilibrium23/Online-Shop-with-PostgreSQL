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
    #home
    path('', home_views.start_page, name = "start_page"),
    path('home/', home_views.home,name = "home"),

    #register and login
    path('login/', register_and_login_views.login,name = "login"),
    path('register/', register_and_login_views.register,name = "register"),

    #admin
    path('admin/', admin.site.urls),
    path('admin_home/', administration_views.home, name = "admin_home"),
    path('admin_home/logout/', administration_views.logout, name = "adm_logout"),
    path('admin_home/manage/', administration_views.manage, name = "manage"),

    #search and filter
    path('home/search/', searching_views.search_items,name = "search"),
    path('home/search/filter/', searching_views.filter_items,name = "search_filter"),

    #basket
    path('home/basket/', user_profile_views.basket,name = "basket"),
    path('home/basket/<int:monitor_id>/', user_profile_views.add_item_to_basket,name = "basket"),
    path('home/basket/order/', user_profile_views.make_order,name = "order"),

    #profile
    path('home/profile/', user_profile_views.profile,name = "profile"),
    path('home/profile/logout/', user_profile_views.logout,name = "logout"),
    path('home/profile/orders', user_profile_views.user_orders,name = "orders"),
    path('home/profile/return/', user_profile_views.return_product,name = "return"),
    path('home/profile/returns/', user_profile_views.show_return_products,name = "returns"),
    path('home/profile/opinions/', user_profile_views.user_opinions,name = "opinions"),
    path('home/profile/opinion/', user_profile_views.add_opinion,name = "opinion"),
    path('home/profile/adresses/', user_profile_views.user_adress,name = "account_details"),
    path('home/profile/adresses/adress/', user_profile_views.set_main_adress,name = "adress"),
    path('home/profile/adresses/adress/delete/', user_profile_views.delete_user_adress,name = "delete"),
]
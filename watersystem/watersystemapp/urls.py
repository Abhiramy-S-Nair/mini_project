from django.urls import path
from watersystemapp import views
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('about.html', views.about, name='about'),
    path('products.html', views.products, name='products'),
    path('blog.html', views.blog, name='blog'),
    path('book.html', views.book, name='book'),
    path('logout/', views.logout, name='logout'),
    path('cleaning.html', views.cleaning, name='cleaning'),
    path('booking.html', views.booking, name='booking'),
    path('contact.html', views.contact, name='contact'),
    path('services.html', views.services, name='services'),
    path('login.html', views.user_login, name='user_login'),
    path('signup.html', views.signup, name='signup'),
    path('admindashboard.html', views.admindashboard, name='admindashboard'),
    path('workerdashboard.html', views.workerdashboard, name='workerdashboard'),
    path('user_list.html', views.user_list, name='user_list'),
    path('worker_list.html', views.worker_list, name='worker_list'),
    
    path('registered_users.html', views.registered_users, name='registered_users'),
    path('user_logout', views.user_logout, name='user_logout'),
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),

]
    

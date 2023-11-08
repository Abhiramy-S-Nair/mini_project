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
    path('request_worker_signup.html', views.request_worker_signup, name='request_worker_signup'),
    path('admin_worker_requests.html', views.admin_worker_requests, name='admin_worker_requests'),
    path('delete_worker/<int:worker_id>/', views.delete_worker, name='delete_worker'),
    path('add_worker.html', views.add_worker, name='add_worker'),
    path('userprofile.html', views.userprofile, name='userprofile'),
    path('waterbooking.html', views.waterbooking, name='waterbooking'),
    path('adddistrict.html', views.adddistrict, name='adddistrict'),
     path('viewrequest.html', views.viewrequest, name='viewrequest'),
    path('addproduct.html', views.addproduct, name='addproduct'),
    path('address.html', views.address, name='address'),
     path('productview.html', views.productview, name='productview'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
     path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('order/', views.order_view, name='order_view'),
     path('book_product/', views.book_product, name='book_product'), 
     path('orderaddress/<int:order_id>/<int:address_id>/', views.orderaddress, name='orderaddress'),
    path('order_address_details/<int:order_id>/', views.order_address_details, name='order_address_details'),
    path('all_orders_details/', views.all_orders_details, name='all_orders_details'),
       path('delete_order/<int:order_id>/', views.delete_order, name='delete_order'),
     path('adding.html', views.adding, name='adding'),
    path('add_city.html', views.add_city, name='add_city'),
    path('add_service.html', views.add_service, name='add_service'),
    path('update_worker_profile/', views.update_worker_profile, name='update_worker_profile'),
     path('service_details.html', views.service_details, name='service_details'),
     path('service_users.html', views.service_users, name='service_users'),
    path('confirm_order/<int:order_id>/', views.confirm_order, name='confirm_order'),
    path('order_confirmation/', views.order_confirmation, name='order_confirmation'),
    path('submit_cleaning_request/', views.submit_cleaning_request, name='submit_cleaning_request'),

     path('upload_file.html', views.upload_file, name='upload_file'),
    path('file_upload_success/', views.file_upload_success, name='file_upload_success'),

    path('view_uploaded_files/', views.view_uploaded_files, name='view_uploaded_files'),
    
    path('activate_user/<int:user_id>/', views.activate_user, name='activate_user'),
    path('deactivate_user/<int:user_id>/', views.deactivate_user, name='deactivate_user'),
    
    path('registered_users.html', views.registered_users, name='registered_users'),
    path('user_logout', views.user_logout, name='user_logout'),
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),

]
    

from django.urls import path
from watersystemapp import views
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('termsforwater.html', views.termsforwater, name='termsforwater'),
    path('termsforcleaning.html', views.termsforcleaning, name='termsforcleaning'),
    path('views.html', views.views, name='views'),
    path('orders.html', views.orders, name='orders'),
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
    path('workmanagerdashboard.html', views.workmanagerdashboard, name='workmanagerdashboard'),
    path('workerdashboard.html', views.workerdashboard, name='workerdashboard'),
    path('user_list.html', views.user_list, name='user_list'),
    path('worker_list.html', views.worker_list, name='worker_list'),
    path('request_worker_signup.html', views.request_worker_signup, name='request_worker_signup'),
    path('admin_worker_requests.html', views.admin_worker_requests, name='admin_worker_requests'),
    path('delete_worker/<int:worker_id>/', views.delete_worker, name='delete_worker'),
    path('add_worker.html', views.add_worker, name='add_worker'),
    path('userprofile.html', views.userprofile, name='userprofile'),
     path('file_details.html', views.file_details, name='file_details'),
    path('edit_file/<int:file_id>/', views.edit_file, name='edit_file'),
    path('delete_file/<int:file_id>/', views.delete_file, name='delete_file'),
    path('add_workmanager.html', views.add_workmanager, name='add_workmanager'),
    path('admin.html', views.admin, name='admin'),
    path('all_worker_profiles/', views.all_worker_profiles, name='all_worker_profiles'),
    
    path('adddistrict.html', views.adddistrict, name='adddistrict'),
     path('viewrequest.html', views.viewrequest, name='viewrequest'),
    path('addproduct.html', views.addproduct, name='addproduct'),
    path('address.html', views.address, name='address'),
     path('productview.html', views.productview, name='productview'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
     path('edit_profile/', views.edit_profile, name='edit_profile'),
     path('drinking_water_products/', views.drinking_water_products, name='drinking_water_products'),
    
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
     path('product_list.html', views.product_list, name='product_list'),
    path('create_order/<int:product_id>/', views.create_order, name='create_order'),
    path('view_water_orders/', views.view_water_orders, name='view_water_orders'),

     path('add_drinking_water.html', views.add_drinking_water, name='add_drinking_water'),
    path('add_drinking_water_success/', views.add_drinking_water_success, name='add_drinking_water_success'),
    
    path('activate_user/<int:user_id>/', views.activate_user, name='activate_user'),
    path('deactivate_user/<int:user_id>/', views.deactivate_user, name='deactivate_user'),
    
    path('registered_users.html', views.registered_users, name='registered_users'),
    path('user_logout', views.user_logout, name='user_logout'),
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    path('assign_worker/<str:district>/', views.assign_worker, name='assign_worker'),
    path('assign_cleaningworker/<str:district>/', views.assign_worker, name='assign_cleaningworker'),
     path('assign_cleaningworker/<str:district>/', views.assign_cleaning_worker, name='assign_cleaning_worker'),
      path('apply_leave/', views.apply_leave, name='apply_leave'),
       path('view_leave_applications/', views.view_leave_applications, name='view_leave_applications'),
        path('approve_or_delete_leave/', views.approve_or_delete_leave, name='approve_or_delete_leave'),
         path('my_leave_details/', views.my_leave_details, name='my_leave_details'),
path('submit_order/', views.submit_order, name='submit_order'),
 path('orders_list/', views.orders_list, name='orders_list'),
    
    path('order/<int:order_id>/delete/', views.delete_order, name='delete_order'),
      path('confirm_order/<int:order_id>/', views.confirm_order, name='confirm_order'),
   
    path('assigning_worker/<int:order_id>/', views.assigning_worker, name='assigning_worker'),
    path('process_assignment/<int:order_id>/', views.process_assignment, name='process_assignment'),
    path('assignment_success/', views.assignment_success, name='assignment_success'),
     path('worker_assignment_details/', views.worker_assignment_details, name='worker_assignment_details'),
      path('complete_order/<int:order_id>/', views.complete_order, name='complete_order'),
      path('order_history/', views.order_history, name='order_history'),
       path('payment_page/<int:order_id>/<str:username>/', views.payment_page, name='payment_page'),
        path('process_payment/<int:order_id>/', views.process_payment, name='process_payment'),
        path('payment_history/', views.payment_history, name='payment_history'),
]



    

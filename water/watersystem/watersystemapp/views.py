from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as auth_logout
from django.http import HttpResponse
from .models import CustomUser
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import render, get_object_or_404 
from .forms import WorkerForm
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from .models import LoginDetail
from .forms import DistrictForm
from .forms import WaterProductForm
from .models import WaterProduct
from .forms import EditProfileForm
from .models import Order
from .forms import OrderForm
from .models import Address
from .forms import AddressForm 
from .forms import OrderAddressForm
from .models import City,District
from django.core.mail import send_mail
from django.conf import settings
from .models import WorkerProfile
from .forms import WorkerProfileForm
from .models import  ServiceRequest
from .forms import CleaningRequestForm
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
 # Import the Order model
# Import your WaterBooking model






def index(request):
    return render(request, 'index.html')

def views(request):
    return render(request, 'views.html')

def orders(request):
    return render(request, 'orders.html')

def viewrequest (request):
    service_requests = ServiceRequest.objects.all()
    return render(request, 'viewrequest.html', {'service_requests': service_requests})
    

def adding(request):
    return render(request, 'adding.html')


from .models import UploadedFile

def file_details(request):
    files = UploadedFile.objects.all()
    return render(request, 'file_details.html', {'files': files})

from django.http import HttpResponse
from .forms import FileEditForm

def edit_file(request, file_id):
    file = get_object_or_404(UploadedFile, pk=file_id)

    if request.method == 'POST':
        form = FileEditForm(request.POST, instance=file)
        if form.is_valid():
            form.save()
            return redirect('file_details')
    else:
        form = FileEditForm(instance=file)

    return render(request, 'edit_file.html', {'form': form, 'file': file})

def delete_file(request, file_id):
    file = get_object_or_404(UploadedFile, pk=file_id)

    if request.method == 'POST':
        file.delete()
        return redirect('file_details')

    return render(request, 'delete_file.html', {'file': file})

def about(request):
    return render(request, 'about.html')

def products(request):
    return render(request, 'products.html')

def blog(request):
    return render(request, 'blog.html')

def add_worker(request):
    return render(request, 'add_worker.html')

def admin(request):
    return render(request, 'admin.html')

def request_worker_signup(request):
    return render(request, 'request_worker_signup.html')

def userprofile(request):
    return render(request, 'userprofile.html')
    

def termsforwater(request):
    return render(request, 'termsforwater.html')

def termsforcleaning(request):
    return render(request, 'termsforcleaning.html')


def admin_worker_requests(request):
    return render(request, 'admin_worker_requests.html')


def adddistrict(request):
     if request.method == 'POST':
        form = DistrictForm(request.POST)
        if form.is_valid():
            form.save()  # This will save the district to the database
            return redirect('adddistrict')  # Redirect to a success page or any other page
     else:
        form = DistrictForm()

        return render(request, 'adddistrict.html', {'form': form})
     


     
def addproduct(request):
     if request.method == 'POST':
        form = WaterProductForm(request.POST)
        if form.is_valid():
            form.save()  # This will save the district to the database
            return redirect('addproduct')  # Redirect to a success page or any other page
     else:
        form = WaterProductForm()

        return render(request, 'addproduct.html', {'form': form})



def book(request):
    if 'username' in request.session:
       response = render(request, 'book.html')
       response['Cache-Control'] = 'no-store, must-revalidate'
       return response
    else:
       return redirect('index')
    #return render(request, 'book.html')

def admindashboard (request):
    if 'username' in request.session:
       response = render(request, 'admindashboard.html')
       response['Cache-Control'] = 'no-store, must-revalidate'
       return response
    else:
       return redirect('index')
    #return render(request, 'admindashboard.html')

def workmanagerdashboard (request):
    if 'username' in request.session:
       response = render(request, 'workmanagerdashboard.html')
       response['Cache-Control'] = 'no-store, must-revalidate'
       return response
    else:
       return redirect('index')
    #return render(request, 'admindashboard.html')

def workerdashboard (request):
    if 'username' in request.session:
       response = render(request, 'workerdashboard.html')
       response['Cache-Control'] = 'no-store, must-revalidate'
       return response
    else:
       return redirect('index')
   # return render(request, 'workerdashboard.html')

def booking (request):
    if 'username' in request.session:
       response = render(request, 'booking.html')
       response['Cache-Control'] = 'no-store, must-revalidate'
       return response
    else:
       return redirect('index')
    #return render(request, 'booking.html')




def user_list(request):
    users = CustomUser.objects.all()
    return render(request, 'user_list.html', {'users': users})


def worker_list(request):
    # Fetch users with the "Worker" role
    workers = CustomUser.objects.filter(role='Worker')

    return render(request, 'worker_list.html', {'users': workers})

def registered_users(request):
    # Fetch users with the "User" role
    users = CustomUser.objects.filter(role='User')

    return render(request, 'registered_users.html', {'users': users})


def contact(request):
    return render(request, 'contact.html')

# @login_required
def services(request):
    if 'username' in request.session:
       response = render(request, 'services.html')
       response['Cache-Control'] = 'no-store, must-revalidate'
       return response
    else:
       return redirect('index')



    # return render(request, 'services.html')

def user_login(request):
    if request.method == "POST":
        # Handle the login form submission
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            user1 = CustomUser.objects.get(username=username)
        except CustomUser.DoesNotExist:
            # User does not exist, handle this case (e.g., display an error message)
            
            
            messages.error(request, "User does not exist. Please register before logging in.")
            return HttpResponse("User does not exist. Please register before logging in.")

        
        user = authenticate(request, username=username, password=password)
        user1=CustomUser.objects.get(username=username)
        if user is not None:
         if user1.role == "Worker":
            # The user is valid, log them in
            login(request, user)
            request.session['username'] = username
            return redirect("workerdashboard")
         elif  user1.role == "User":
            login(request,user)
            request.session['username'] = username
            return redirect("services") 
         elif  user1.role == "workmanager":
            login(request,user)
            request.session['username'] = username
            return redirect("workmanagerdashboard")  
         elif  user1.username == "abhi":
            login(request,user)
            request.session['username'] = username
            return redirect("admindashboard")
        else:
                # Handle the case where the user is anonymous
                messages.error(request, "User does not exist. Please register before logging in.")
    else:
            # Authentication failed, show an error message
         messages.error(request, "Incorrect username or password. Please try again.")

    response = render(request, 'login.html')
    response['Cache-Control'] = 'no-store, must-revalidate'
    return response



    #         # Authentication failed, handle the error or show a message
    #         return HttpResponse("Login failed. Please check your username and password.")
    
    # # Handle the GET request (display the login form)
    # return render(request, "login.html")



def signup(request):
    if request.method == "POST":
        # Extract form data
        username = request.POST.get('username', None)
        email = request.POST.get('email', None)
        password = request.POST.get('password1', None)
        role = request.POST.get('role', None)
        first_name = request.POST.get('first_name', None)
        last_name = request.POST.get('last_name', None)

        if username and email and password and role:
            # Check if the username or email is already registered
            if CustomUser.objects.filter(username=username).exists():
                messages.error(request, "Username already registered.")
            elif CustomUser.objects.filter(email=email).exists():
                messages.error(request, "Email already registered.")
            else:
                # Create a new CustomUser instance
                user = CustomUser.objects.create_user(
                    username=username,
                    email=email,
                    role=role,
                    first_name=first_name,
                    last_name=last_name,
                    password=password,
                )
                # Log in the user after registration
                login(request, user)
               

                # Redirect to the signup page to display the message

                return redirect('index')
        else:
            messages.error(request, "Please fill in all the required fields.")
    
    # If the request method is not POST or there was an error, render the signup form
    return render(request, "signup.html")

    
def user_logout(request):
    try:
        del request.session['username']
    except:
        return redirect('user_login')
    return redirect('user_login')
    
def logout(request):
    auth_logout(request) # Use the logout function to log the user out
    return redirect('index')  # Redirect to the confirmation page


   

 

def delete_worker(request, worker_id):
    worker = get_object_or_404(CustomUser, pk=worker_id)
    
    if request.method == 'POST':
        worker.delete()
        messages.success(request, f'Worker {worker.username} has been deleted.')
        return redirect('worker_list')
    
    return render(request, 'delete_worker.html', {'worker': worker})
      
def add_worker(request):
    if request.method == 'POST':
        form = WorkerForm(request.POST)  # If you have a form, initialize it with POST data
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            # Redirect or perform other actions
            subject = 'Registration Confirmation'
            message = f'welcome to our family \n\n Username: {user.username}\nPassword: {password} \n With regards, \n Team Waterain '
            from_email = settings.EMAIL_HOST_USER  # Use your email add ress as the sender
            recipient_list = [user.email]  # Doctor's email address

            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            return redirect('worker_list')
    else:
        form = WorkerForm()  # If it's a GET request, create an empty form
    return render(request, 'add_worker.html', {'form': form})


@receiver(user_logged_in)
def save_login_detail(sender, request, user, **kwargs):
    # Create and save a new LoginDetail instance
    LoginDetail.objects.create(username=user)


def productview(request):
    products = WaterProduct.objects.all()
    return render(request, 'productview.html', {'products': products})

def delete_product(request, product_id):
    if request.method == 'POST':
        # Find the product to delete
        product = WaterProduct.objects.get(product_id=product_id)
        # Delete the product
        product.delete()
        # Redirect to the product list page
        return redirect('productview')  # Replace 'product_list' with the name of your product list view

    return redirect('productview') 

    


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()  # This will update the user's data in the database
            return redirect('userprofile')  # Redirect to the user's profile page
    else:
        form = EditProfileForm(instance=request.user)

    context = {
        'form': form,
    }

    return render(request, 'edit_profile.html', context)




def book_product(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            # Assuming you want to associate the address with the currently logged-in user
            address.user = request.user  # You need to import CustomUser model if not already imported
            address.save()
            return redirect('services')  # Redirect to a success page
    else:
        form = AddressForm()

    context = {
        'form': form,
    }
    return render(request, 'address.html', context)


def address(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            # Create a new Address object and save it to the database
            address = form.save(commit=False)
            # Assuming you want to associate the address with the currently logged-in user
            address.user = request.user  # You need to import CustomUser model if not already imported
            address.save()

            # Redirect to a success page or any other page
            return redirect('services')  # Change 'success_page' to the actual page name
        else:
            print(form.errors)  # For debugging, handle form errors
    else:
        initial_data = {
            'user': request.user,  # Pre-fill the logged-in user
        }
        form = AddressForm(initial=initial_data)

    return render(request, 'address.html', {'form': form})





def orderaddress(request, order_id, address_id):
    # Fetch the Order and Address instances based on the provided IDs
    order = Order.objects.get(order_id=order_id)
    address = Address.objects.get(address_id=address_id)

    if request.method == 'POST':
        form = OrderAddressForm(request.POST)
        if form.is_valid():
            order_address = form.save(commit=False)
            order_address.order = order
            order_address.address = address
            order_address.save()
            return redirect('services')  # Redirect to the order view or any other page
    else:
        form = OrderAddressForm(initial={'order': order, 'address': address})

    context = {
        'form': form,
        'order': order,
        'address': address,
    }

    return render(request, 'orderaddress.html', context)

def order_address_details(request, order_id):
    # Fetch the Order instance based on the provided order_id
    order = Order.objects.get(order_id=order_id)
    
    # Render the HTML template with the order details
    return render(request, 'order_address_details.html', {'order': order})


from django.shortcuts import render
from .models import Order

def all_orders_details(request):
    orders = Order.objects.all()

    # Create a list to store order and address details
    order_details = []

    # Iterate through the orders and fetch the associated address for each order
    for order in orders:
        order_detail = {
            'order_id': order.order_id,
            'user': order.user.username,
            'product_name': order.product.product_name,
            'product_price': order.product.price,
            'quantity': order.quantity,
        }

        # Fetch the associated address for the order
        address = order.user.address_set.first()
        if address:
            order_detail['mobile_number'] = address.mobile_number
            order_detail['pincode'] = address.pincode
            order_detail['City_ID'] = address.City_ID.city_name
            order_detail['street'] = address.street
            order_detail['district_name'] = address.district.district_name

        order_details.append(order_detail)

    return render(request, 'all_orders_details.html', {'order_details': order_details})





def delete_order(request, order_id):
    # Fetch the order based on the order_id from the URL
    order = get_object_or_404(Order, order_id=order_id)

    # Add your logic for deleting the order (e.g., order.delete())

    # Redirect to the page where you want to display the updated order list
    return redirect('all_orders_details')







from django.shortcuts import render, redirect
from .models import Order, Address

def confirm_order(request, order_id):
    # Retrieve the order and address details based on the 'order_id'
    order = Order.objects.get(order_id=order_id)
    
    # Retrieve the associated address for the given order
    try:
        address = Address.objects.get(order=order)
    except Address.DoesNotExist:
        # Handle the case where no address is associated with the order
        address = None
    
    # Your confirmation logic goes here

    # Pass the order and address details to the 'order_confirmation' template
    context = {
        'order_detail': order,
        'address_detail': address,
    }

    return render(request, 'order_confirmation.html', context)



def order_confirmation(request):
    return render(request, 'order_confirmation.html')



def add_city(request):
    if request.method == 'POST':
        city_name = request.POST['city_name']
        City.objects.create(city_name=city_name)  # Corrected field name
        return redirect('adding')  # Redirect to a success page

    return render(request, 'add_city.html')


#active and deactive of user
def deactivate_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    if user.is_active:
        user.is_active = False
        user.save()
         # Send deactivation email
        subject = 'Account Deactivation'
        message = 'Your account has been deactivated by the admin.'
        from_email = 'abhiramysnair2024a@mca.ajce.in'  # Replace with your email
        recipient_list = [user.email]
        html_message = render_to_string('deactivation_mail.html', {'user': user})

        send_mail(subject, message, from_email, recipient_list, html_message=html_message)

        messages.success(request, f"User '{user.username}' has been deactivated, and an email has been sent.")
    else:
        messages.warning(request, f"User '{user.username}' is already deactivated.")
    return redirect('admindashboard')

def activate_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    if not user.is_active:
        user.is_active = True
        user.save()
        subject = 'User Activation'
        message = f'Dear member of Waterain , \n your account has been activated\n With regards, \n Team Waterain '
        from_email = settings.EMAIL_HOST_USER  # Use your email add ress as the sender
        recipient_list = [user.email]  # Doctor's email address

        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        return redirect('admindashboard')
    else:
        messages.warning(request, f"User '{user.username}' is already active.")
    return redirect('admindashboard')




def update_worker_profile(request):
    if request.method == 'POST':
        form = WorkerProfileForm(request.POST, request.FILES)
        if form.is_valid():
            worker_profile = form.save(commit=False)
            worker_profile.user = request.user
            worker_profile.save()
            messages.success(request, 'Worker profile updated successfully!')
            return redirect('workerdashboard')
        else:
            messages.error(request, 'Please correct the errors in the form.')
            print(form.errors)
    else:
        form = WorkerProfileForm()

    return render(request, 'update_worker_profile.html', {'form': form, 'messages': messages.get_messages(request)})

from .forms import AddServiceForm  # Import the form you created
from .models import AddService


def add_service(request):
    if request.method == 'POST':
        form = AddServiceForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            form.save()
            messages.success(request, 'Service added successfully!')
            return redirect('admindashboard')  # Replace 'services' with the URL where you list your services
        else:
            messages.error(request, 'Please correct the errors in the form.')
    else:
        form = AddServiceForm()

    return render(request, 'add_service.html', {'form': form})


def service_details(request):
    services = AddService.objects.all()
    return render(request, 'service_details.html', {'services': services})

def service_users(request):
    services = AddService.objects.all()
    return render(request, 'service_users.html', {'services': services})





from django.http import HttpResponse

def submit_cleaning_request(request):
    if request.method == 'POST':
         
         form = CleaningRequestForm(request.POST)
         if form.is_valid():
            ServiceRequest = form.save(commit=False)
            ServiceRequest.user = request.user  # Set the user from the request
            ServiceRequest.save()
            return redirect('service_users')
        # Fetch the logged-in user
         
    else:
        form = CleaningRequestForm()

    user = request.user
        # Fetch the selected service_name from URL parameters
    service_name = request.GET.get('service_name', '')

    try:
            # Get the service object based on the service_name
            service = AddService.objects.get(name=service_name)
    except AddService.DoesNotExist:
            # Handle the case where the service doesn't exist
            # You can redirect or display an error message
            print(f"Service not found: {service_name}")
            return redirect('cleaning')

        # Fetch other form fields
    length = request.POST.get('length', None)
    width = request.POST.get('width', None)
    water_level = request.POST.get('waterLevel', None)
    street = request.POST['street']
    city_id = request.POST['city']
    district_id = request.POST['district']
    zip_code = request.POST['zipCode']
    request_date_time = request.POST['requestDateTime']

        # Add some print statements to check form data
    print(f"Service: {service_name}")
    print(f"Length: {length}")
    print(f"Width: {width}")
    print(f"Water Level: {water_level}")
    print(f"Street: {street}")
    print(f"City: {city_id}")
    print(f"District: {district_id}")
    print(f"ZIP Code: {zip_code}")
    print(f"Request Date Time: {request_date_time}")

        # Create a new ServiceRequest object and save it to the database
    service_request = ServiceRequest(
            user=user,
            service_name=service,
            length=length,
            width=width,
            water_level=water_level,
            street=street,
            city_id=city_id,
            district_id=district_id,
            zip_code=zip_code,
            request_date_time=request_date_time,
        )
    service_request.save()

        # You can add any additional logic or redirect to a success page here
    return redirect('services')

    # Handle the case where the request method is not POST

  






def cleaning(request):
    service_name = request.GET.get('service_name', '')  # Retrieve the 'service_name' from URL parameters

    try:
        service = AddService.objects.get(name=service_name)  # Get the service object based on the service name

        # Pre-fill the form with the selected service
        initial_data = {
            'user': request.user,
            'service_name': service,
        }
    except AddService.DoesNotExist:
        initial_data = {}

    if request.method == 'POST':
        form = CleaningRequestForm(request.POST, initial=initial_data)
        if form.is_valid():
            form.save()
            return redirect('services')  # Redirect to a success page
    else:
        form = CleaningRequestForm(initial=initial_data)

    context = {
        'form': form,
    }

    return render(request, 'cleaning.html', context)


from .models import UploadedFile
from .forms import UploadFileForm



def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            description = form.cleaned_data['description']
            pdf_file = form.cleaned_data['pdf_file']
            
            uploaded_file = UploadedFile(description=description, pdf_file=pdf_file)
            uploaded_file.save()

            # You can add any additional logic here (e.g., redirect to a success page)
            return redirect('file_upload_success')  # Use the URL pattern name

    else:
        form = UploadFileForm()

    return render(request, 'upload_file.html', {'form': form})

def file_upload_success(request):
    return render(request, 'file_upload_success.html')


def view_uploaded_files(request):
    uploaded_files = UploadedFile.objects.all()
    return render(request, 'view_uploaded_files.html', {'uploaded_files': uploaded_files})



from .models import DrinkingWaterProduct

from .forms import DrinkingWaterProductForm

def add_drinking_water(request):
    if request.method == 'POST':
        form = DrinkingWaterProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_drinking_water_success')
    else:
        form = DrinkingWaterProductForm()

    return render(request, 'add_drinking_water.html', {'form': form})

def add_drinking_water_success(request):
    return render(request, 'add_drinking_water_success.html')


from django.shortcuts import render, redirect
from .models import DrinkingWaterProduct
from .models import WaterOrder

from .forms import WaterOrderForm

def product_list(request):
    products = DrinkingWaterProduct.objects.all()
     
    return render(request, 'product_list.html', {'products': products})

@login_required
def create_order(request, product_id):
    product = DrinkingWaterProduct.objects.get(pk=product_id)

    if request.method == 'POST':
        form = WaterOrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if product.reduce_stock(order.quantity):
                order.product = product
                order.user = request.user  # Pre-fill the 'user' field with the current user
                order.save()
                return redirect('product_list')
    else:
        form = WaterOrderForm(initial={'user': request.user, 'product': product})
        # Pre-fill the 'user' and 'product' fields in the form

    return render(request, 'create_order.html', {'form': form, 'product': product})


from .models import WaterOrder

def view_water_orders(request):
    water_orders = WaterOrder.objects.all()
    return render(request, 'view_water_orders.html', {'water_orders': water_orders})


def drinking_water_products(request):
    products = DrinkingWaterProduct.objects.all()
    return render(request, 'drinking_water_products.html', {'products': products})



from django.shortcuts import render, get_object_or_404
from .models import WorkerProfile

def worker_profile_view(request):
    # Attempt to retrieve the WorkerProfile for the user, or return a 404 error if it doesn't exist
    worker_profile = get_object_or_404(WorkerProfile, user=request.user)

    context = {
        'user': request.user,
        'worker_profile': worker_profile,
    }

    return render(request, 'workerdashboard.html', context)

def add_workmanager(request):
    if request.method == "POST":
        # Extract form data
        username = request.POST.get('username', None)
        email = request.POST.get('email', None)
        password = request.POST.get('password1', None)
        role = request.POST.get('role', None)
        first_name = request.POST.get('first_name', None)
        last_name = request.POST.get('last_name', None)

        if username and email and password and role:
            # Check if the username or email is already registered
            if CustomUser.objects.filter(username=username).exists():
                messages.error(request, "Username already registered.")
            elif CustomUser.objects.filter(email=email).exists():
                messages.error(request, "Email already registered.")
            else:
                # Create a new CustomUser instance
                user = CustomUser.objects.create_user(
                    username=username,
                    email=email,
                    role=role,
                    first_name=first_name,
                    last_name=last_name,
                    password=password,
                )
                # Log in the user after registration
                login(request, user)
               

                # Redirect to the signup page to display the message

                return redirect('index')
        else:
            messages.error(request, "Please fill in all the required fields.")
    
    # If the request method is not POST or there was an error, render the signup form
    return render(request, "add_workmanager.html")

from django.shortcuts import render
from .models import WorkerProfile, CustomUser

def all_worker_profiles(request):
    try:
        worker_profiles = WorkerProfile.objects.all()
        user_details = CustomUser.objects.filter(id__in=[profile.user_id for profile in worker_profiles])

        worker_data = []
        for worker_profile, user_detail in zip(worker_profiles, user_details):
            worker_data.append({
                'worker_id': worker_profile.worker_id,
                'profile_picture': worker_profile.profile_picture.url,
                'gender': worker_profile.gender,
                'mobile_number': worker_profile.mobile_number,
                'district': worker_profile.district,
                'bio': worker_profile.bio,
                'services': worker_profile.services,
                'experience': worker_profile.experience,
                'availability': worker_profile.availability,
                'terms': worker_profile.terms,
                'username': user_detail.username,
                'firstname': user_detail.firstname,
                'lastname': user_detail.lastname,
                'email': user_detail.email,
                'role': user_detail.role,
            })

        return render(request, 'all_worker_profiles.html', {'worker_data': worker_data})
    except WorkerProfile.DoesNotExist:
        # Handle the case when no worker profiles exist
        return render(request, 'all_worker_profiles.html', {'error_message': 'No worker profiles exist'})

def assign_worker(request, district):
    # Get the District object based on the district name
    district_object = get_object_or_404(District, district_name=district)

    # Get available workers in the same district
    available_workers = WorkerProfile.objects.filter(district=district_object)

    # Pass the data to the template
    context = {'district': district_object, 'available_workers': available_workers}

    return render(request, 'assign_worker.html', context)

# views.py
#from django.shortcuts import render, redirect
from .models import ServiceRequest, AssignedWorker
from .forms import AssignWorkerForm

def assign_cleaning_worker(request, district):
    # Fetch the service requests for the specified district
    service_requests = ServiceRequest.objects.filter(district__district_name=district)

    if request.method == 'POST':
        form = AssignWorkerForm(request.POST)
        if form.is_valid():
            selected_workers = form.cleaned_data['selected_workers']
            service_request_id = form.cleaned_data['service_request_id']

            # Create AssignedWorker instances for each selected worker
            for worker in selected_workers:
                AssignedWorker.objects.create(
                    service_request_id=service_request_id,
                    worker=worker,
                    work_status='pending'
                )

            return redirect('viewrequest.html')  # Redirect to the service requests page after confirmation
    else:
        form = AssignWorkerForm()

    context = {
        'form': form,
        'service_requests': service_requests,
        'district': district,
    }

    return render(request, 'assign_cleaning_worker.html', context)


# views.py
from django.shortcuts import render, redirect
from .forms import LeaveApplicationForm

def apply_leave(request):
    if request.method == 'POST':
        form = LeaveApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            # Process the form data and save the leave application
            leave_application = form.save(commit=False)
            leave_application.user = request.user
            leave_application.save()

            return redirect('workerdashboard')  # Redirect to the dashboard after submission
    else:
        form = LeaveApplicationForm()

    return render(request, 'apply_leave.html', {'form': form})
from .models import LeaveApplication
def view_leave_applications(request):
    leave_applications = LeaveApplication.objects.all()
    return render(request, 'view_leave_applications.html', {'leave_applications': leave_applications})
from django.http import JsonResponse


def approve_or_delete_leave(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        application_id = request.POST.get('application_id')

        if action == 'approve':
            LeaveApplication.objects.filter(leave_application_id=application_id, status='pending').update(status='approved')

        elif action == 'delete':
            LeaveApplication.objects.filter(leave_application_id=application_id, status='pending').update(status='deleted')

    return redirect('view_leave_applications')

@login_required
def my_leave_details(request):
    user = request.user
    leave_details = LeaveApplication.objects.filter(user=user)
    return render(request, 'my_leave_details.html', {'leave_details': leave_details})
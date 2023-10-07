from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as auth_logout
from django.http import HttpResponse
from .models import CustomUser
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def products(request):
    return render(request, 'products.html')

def blog(request):
    return render(request, 'blog.html')


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

def cleaning (request):
    if 'username' in request.session:
       response = render(request, 'cleaning.html')
       response['Cache-Control'] = 'no-store, must-revalidate'
       return response
    else:
       return redirect('index')
    #return render(request, 'cleaning.html')


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
            return HttpResponse("User does not exist. Please register before logging in.")

        
        user = authenticate(request, username=username, password=password)
        user1=CustomUser.objects.get(username=username)
        if user1.role == "Worker":
            # The user is valid, log them in
            login(request, user)
            request.session['username'] = username
            return redirect("workerdashboard")
        elif  user1.role == "User":
            login(request,user)
            request.session['username'] = username
            return redirect("services")  
        elif  user1.username == "abhi":
            login(request,user)
            request.session['username'] = username
            return redirect("admindashboard")
        else:
            messages.error(request, "Invalid login credentials")

    response = render(request, 'login.html')
    response['Cache-Control'] = 'no-store, must-revalidate'
    return response



    #         # Authentication failed, handle the error or show a message
    #         return HttpResponse("Login failed. Please check your username and password.")
    
    # # Handle the GET request (display the login form)
    # return render(request, "login.html")

def signup(request):
    if request.method == "POST":
            # Extract custom fields from the form
            username = request.POST["username"]
            email = request.POST["email"]
            password = request.POST["password1"]
            role = request.POST["role"]
            first_name = request.POST["first_name"]
            last_name = request.POST["last_name"]
            if (
            CustomUser.objects.filter(username=username).exists()
            or CustomUser.objects.filter(email=email).exists()
            ):
                messages.error(request, "Email Already Registered")
                return render(request, "signup.html")
            else:
    
          
                # Create a CustomUser instance
                user = CustomUser.objects.create_user(
                   username=username,
                   email=email,
                   role=role,
                   first_name=first_name,
                   last_name=last_name,
                   password=password,
               )
                user.save()
                

            # Log in the user after registration
            login(request, user)
            return redirect("index")  
    else:

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
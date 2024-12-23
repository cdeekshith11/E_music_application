# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.models import User
# from django.contrib import messages
# from django.contrib.auth.decorators import login_required
# from accounts.models import Genre, Notification, SongCategory, SubscriptionPlan

# def home(request):
#     return render(request, 'accounts/home.html')
# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('dashboard')  # Redirect to the dashboard after login
#         else:
#             messages.error(request, 'Invalid username or password.')
#     return render(request, 'accounts/login.html')


# def signup_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         confirm_password = request.POST['confirm_password']

#         if password != confirm_password:
#             messages.error(request, 'Passwords do not match.')
#         else:
#             try:
#                 user = User.objects.create_user(username=username, password=password)
#                 user.save()
#                 messages.success(request, 'Account created successfully. Please log in.')
#                 return redirect('login')
#             except:
#                 messages.error(request, 'Username already exists.')
#     return render(request, 'accounts/signup.html')

# @login_required
# def dashboard(request):
#     return render(request, 'accounts/dashboard.html')

# def about_us(request):
#     return render(request, 'accounts/about_us.html')
# def contact_us(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         email = request.POST['email']
#         message = request.POST['message']
#         # You can process the data or save it to the database here
#         messages.success(request, 'Thank you for reaching out. We will get back to you soon.')
#         return redirect('contact')

#     return render(request, 'accounts/contact_us.html')
# def subscription_plans(request):
#     plans = SubscriptionPlan.objects.all()
#     return render(request, 'accounts/subscription_plans.html', {'plans': plans})

# def categories(request):
#     categories = SongCategory.objects.all()
#     return render(request, 'accounts/categories.html', {'categories': categories})

# def genres(request, category_id):
#     genres = Genre.objects.filter(category_id=category_id)
#     return render(request, 'accounts/genres.html', {'genres': genres})


# @login_required
# def notifications(request):
#     notifications = Notification.objects.filter(user=request.user).order_by('-created_at')
#     return render(request, 'accounts/notifications.html', {'notifications': notifications})
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from accounts.models import Genre, Notification, SongCategory, SubscriptionPlan

def home(request):
    return render(request, 'accounts/home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to the dashboard after login
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'accounts/login.html')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
        else:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists.')
            else:
                User.objects.create_user(username=username, password=password)
                messages.success(request, 'Account created successfully. Please log in.')
                return redirect('login')
    return render(request, 'accounts/signup.html')

@login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html')

def about_us(request):
    return render(request, 'accounts/about_us.html')

def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        messages.success(request, 'Thank you for reaching out. We will get back to you soon.')
        return redirect('contact')
    return render(request, 'accounts/contact_us.html')

def subscription_plans(request):
    plans = SubscriptionPlan.objects.all()
    return render(request, 'accounts/subscription_plans.html', {'plans': plans})

def categories(request):
    categories = SongCategory.objects.all()
    return render(request, 'accounts/categories.html', {'categories': categories})

def genres(request, category_id):
    genres = Genre.objects.filter(category_id=category_id)
    return render(request, 'accounts/genres.html', {'genres': genres})

@login_required
def notifications(request):
    notifications = Notification.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'accounts/notifications.html', {'notifications': notifications})

# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login
# from django.contrib.auth.models import User
# from django.contrib import messages
# from django.contrib.auth.decorators import login_required
# from accounts.models import Genre, Notification, SongCategory, SubscriptionPlan

# def home(request):
#     return render(request, 'accounts/home.html')

# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('dashboard')  # Redirect to the dashboard after login
#         else:
#             messages.error(request, 'Invalid username or password.')
#     return render(request, 'accounts/login.html')

# def signup_view(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         confirm_password = request.POST.get('confirm_password')

#         if password != confirm_password:
#             messages.error(request, 'Passwords do not match.')
#         else:
#             if User.objects.filter(username=username).exists():
#                 messages.error(request, 'Username already exists.')
#             else:
#                 User.objects.create_user(username=username, password=password)
#                 messages.success(request, 'Account created successfully. Please log in.')
#                 return redirect('login')
#     return render(request, 'accounts/signup.html')

# @login_required
# def dashboard(request):
#     return render(request, 'accounts/dashboard.html')

# def about_us(request):
#     return render(request, 'accounts/about_us.html')

# def contact_us(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         message = request.POST.get('message')
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
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import requests
from django.conf import settings
from django.shortcuts import redirect, render
from django.contrib.auth import update_session_auth_hash
from django.http import HttpResponseNotFound

def home_view(request):
    return render(request, 'accounts/home.html')

def dashboard_view(request):
    return render(request, 'accounts/dashboard.html')

def about_view(request):
    return render(request, 'accounts/about_us.html')

def contact_view(request):
    return render(request, 'accounts/contact_us.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        messages.error(request, 'Invalid credentials')
    return render(request, 'accounts/login.html')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not User.objects.filter(username=username).exists():
            User.objects.create_user(username=username, password=password)
            messages.success(request, 'Account created')
            return redirect('login')
        messages.error(request, 'Username already exists')
    return render(request, 'accounts/signup.html')

def logout_view(request):
    logout(request)
    return redirect('home')
def learn_view(request):
    return render(request, 'accounts/learn.html')
def spotify_login(request):
    client_id = settings.SPOTIFY_CLIENT_ID
    redirect_uri = settings.SPOTIFY_REDIRECT_URI
    scope = "user-read-private user-read-email"  # Add the necessary scope
    spotify_url = (
        f"https://accounts.spotify.com/authorize?"
        f"response_type=code&client_id={client_id}&redirect_uri={redirect_uri}&scope={scope}"
    )
    return redirect(spotify_url)


# Handle Callback from Spotify
def spotify_callback(request):
    code = request.GET.get("code")
    client_id = settings.SPOTIFY_CLIENT_ID
    client_secret = settings.SPOTIFY_CLIENT_SECRET
    redirect_uri = settings.SPOTIFY_REDIRECT_URI

    # Exchange code for an access token
    token_url = "https://accounts.spotify.com/api/token"
    payload = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": redirect_uri,
        "client_id": client_id,
        "client_secret": client_secret,
    }
    response = requests.post(token_url, data=payload)
    token_data = response.json()

    # Access the token (save it for further API calls)
    access_token = token_data.get("access_token")
    refresh_token = token_data.get("refresh_token")

    # Use the access token to fetch Spotify data
    headers = {"Authorization": f"Bearer {access_token}"}
    user_profile_url = "https://api.spotify.com/v1/me"
    user_profile_response = requests.get(user_profile_url, headers=headers)
    user_data = user_profile_response.json()

    return render(request, "spotify_dashboard.html", {"user_data": user_data})
def spotify_dashboard(request):
    # Your logic for the Spotify dashboard
    return render(request, 'accounts/spotify_dashboard.html')
def help_center_view(request):
    return render(request,'accounts/help_center.html')
def settings_view(request):
    return render(request,'accounts/settings.html')
def update_settings(request):
    if request.method == 'POST':
        user = request.user
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.save()
        return redirect('settings')  
    return render(request, 'accounts/settings.html')
def update_settings(request):
    if request.method == "POST":
        user = request.user
        username = request.POST.get("username")
        email = request.POST.get("email")
        current_password = request.POST.get("current_password")
        new_password = request.POST.get("new_password")
        subscription = request.POST.get("subscription")

        # Update username and email
        user.username = username
        user.email = email

        # Update password if provided
        if new_password:
            if user.check_password(current_password):
                user.set_password(new_password)
                update_session_auth_hash(request, user)  # Prevent logout
                messages.success(request, "Password updated successfully.")
            else:
                messages.error(request, "Current password is incorrect.")
                return redirect("settings")

        # Save changes
        user.save()
        messages.success(request, "Settings updated successfully.")
        return redirect("settings")
    
    return render(request, "accounts/settings.html")
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('dashboard')  # Redirect to the dashboard after login
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'accounts/login.html')

def genre_redirect(request, genre):
    # List of supported genres in lowercase, modify this list as per your needs
    supported_genres = ['pop', 'rock', 'jazz', 'classical', 'hiphop','edmfrom django.http import HttpResponseNotFound']

    # Convert genre to lowercase to avoid case sensitivity issues
    genre = genre.lower()

    # Check if the genre is valid
    if genre in supported_genres:
        # Redirect to Spotify's genre page
        return redirect(f'https://open.spotify.com/genre/{genre}')
    else:
        # If the genre is not valid, return a 404 error page
        return HttpResponseNotFound("Genre not found")
def genre_view(request, genre_name):
    print(f"Genre Name: {genre_name}")  # Debugging line
    supported_genres = ['pop', 'rock', 'jazz', 'classical', 'hiphop', 'folk']
    if genre_name.lower() in supported_genres:
        return redirect(f'https://open.spotify.com/genre/{genre_name.lower()}')
    else:
        return HttpResponseNotFound("Genre not found")
def payment_page(request):
    return render(request, 'accounts/payment_page.html')
def subscription_view(request):
    return render(request, 'accounts/subscription.html')

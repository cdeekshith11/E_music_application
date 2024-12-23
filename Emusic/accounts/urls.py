# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home, name='home'),  # Home page
#     path('login/', views.login_view, name='login'),  # Login page
#     path('signup/', views.signup_view, name='signup'),  # Signup page
#     path('dashboard/', views.dashboard, name='dashboard'),
#     path('about/', views.about_us, name='about'),
#     path('contact/', views.contact_us, name='contact'),
#     path('subscriptions/', views.subscription_plans, name='subscriptions'),
#     path('categories/', views.categories, name='categories'),
#     path('categories/<int:category_id>/genres/', views.genres, name='genres'),
#     path('notifications/', views.notifications, name='notifications'),

# ]


from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('login/', views.login_view, name='login'),  # Login page
    path('signup/', views.signup_view, name='signup'),  # Signup page
    path('dashboard/', views.dashboard, name='dashboard'),
    path('about/', views.about_us, name='about'),
    path('contact/', views.contact_us, name='contact'),
    path('subscriptions/', views.subscription_plans, name='subscriptions'),
    path('categories/', views.categories, name='categories'),
    path('categories/<int:category_id>/genres/', views.genres, name='genres'),
    path('notifications/', views.notifications, name='notifications'),
]
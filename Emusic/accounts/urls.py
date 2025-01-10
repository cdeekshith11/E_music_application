from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('learn/', views.learn_view, name='learn'),  # Add this line
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path("spotify/login/", views.spotify_login, name="spotify_login"),
    path("spotify/callback/", views.spotify_callback, name="spotify_callback"),
    path('spotify_dashboard/', views.spotify_dashboard, name='spotify_dashboard'),
    path('songs/', views.spotify_login, name='spotify_login'),  # This will trigger Spotify login
    path('spotify/callback/', views.spotify_callback, name='spotify_callback'),
    path('spotify_dashboard/', views.spotify_dashboard, name='spotify_dashboard'),
    path('help_center/',views.help_center_view,name='help_center'),
    path('settings/', views.settings_view, name='settings'),
    path('settings/update/', views.update_settings, name='update_settings'),
     path('genre/<str:genre_name>/', views.genre_view, name='genre'),
       path('subscription/', views.subscription_view, name='subscription'),
    path('payment/', views.payment_page, name='payment_page'),
    path('spotify/login/', views.spotify_login, name='spotify-login'),
    path('spotify/callback/', views.spotify_callback, name='spotify-callback'),
    path('dashboard/', views.fetch_dashboard_data, name='dashboard'),
    path('notifications/', views.notifications_view, name='notifications'),

]


# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home_view, name='home'),
#     path('dashboard/', views.fetch_dashboard_data, name='dashboard'),
#     path('about/', views.about_view, name='about'),
#     path('contact/', views.contact_view, name='contact'),
#     path('learn/', views.learn_view, name='learn'),
#     path('login/', views.login_view, name='login'),
#     path('signup/', views.signup_view, name='signup'),
#     path('logout/', views.logout_view, name='logout'),
#     path('spotify/login/', views.spotify_login, name='spotify-login'),
#     path('spotify/callback/', views.spotify_callback, name='spotify-callback'),
#     path('spotify_dashboard/', views.spotify_dashboard, name='spotify_dashboard'),
#     path('help_center/', views.help_center_view, name='help_center'),
#     path('settings/', views.settings_view, name='settings'),
#     path('settings/update/', views.update_settings, name='update_settings'),
#     path('genre/<str:genre_name>/', views.genre_view, name='genre'),
#     path('subscription/', views.subscription_view, name='subscription'),
#     path('payment/', views.payment_page, name='payment_page'),
# ]

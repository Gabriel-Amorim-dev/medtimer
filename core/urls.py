from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('', include('users.urls')),
    path('medicamentos/', include('medications.urls')),
    path('doses/', include('doses.urls')),
    path('tratamentos/', include('treatments.urls')),
    path('notificacoes/', include('notifications.urls')),
    path('login/',  auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

]


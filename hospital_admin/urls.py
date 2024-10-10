from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('', views.admin_login, name='admin-login'),
    path('forgot-password/', views.admin_forgot_password,name='admin_forgot_password'),
    path('login/',views.admin_login,name='admin_login'),
    path('admin_register/',views.admin_register,name='admin_register'),
    path('admin-logout/', views.logoutAdmin, name='admin-logout'),    
]
  


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

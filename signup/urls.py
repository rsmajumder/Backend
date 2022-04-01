from django.urls import re_path,include,path

from .views import RegisterAPI,ChangePasswordView,UserProfileAPI,OTPLogin,OTPCheck
from knox import views as knox_views
from .views import LoginAPI
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    re_path(r'register/$', RegisterAPI.as_view(), name='register'),
    re_path(r'userprofile/$',UserProfileAPI.as_view(),name='userprofile'),
    path(r'login/', LoginAPI.as_view(), name='login'),
    re_path(r'logout/$', knox_views.LogoutView.as_view(), name='logout'),
    re_path(r'logoutall/$', knox_views.LogoutAllView.as_view(), name='logoutall'),
    re_path(r'change-password/$', ChangePasswordView.as_view(), name='change-password'),
    re_path(r'password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    re_path(r'otp/$',OTPLogin.as_view(),name='otpLogin'),
    re_path(r'otpcheck/$',OTPCheck.as_view(),name='otpCheck')

]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
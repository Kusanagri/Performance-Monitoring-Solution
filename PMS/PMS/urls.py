from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from myapp import views as core_views

urlpatterns = [
    url(r'^$', core_views.home, name='home'),
    url(r'^login/$', auth_views.LoginView.as_view(), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),  # <--
    url(r'^admin/', admin.site.urls),
]
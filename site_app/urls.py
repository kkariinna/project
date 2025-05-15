from django.contrib import admin
from django.urls import path
from .import views

app_name = 'site_app'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.first_page),
    path('page/<int:pk>', views.page, name='page'),
 ]

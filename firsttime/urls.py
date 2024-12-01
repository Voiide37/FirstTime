from django.contrib import admin
from django.urls import path, include
from todolist_app import views as todolistviews
from users_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', todolistviews.index, name='index'),
    path('task/', include('todolist_app.urls')),
    path('account/', include('users_app.urls')),
    path('contact/', todolistviews.contact, name='contact'),
    path('about/', todolistviews.about, name='about'),
]

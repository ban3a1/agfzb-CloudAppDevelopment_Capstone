from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # route is a string contains a URL pattern
    # view refers to the view function
    # name the URL
    path(route='', view=views.index, name='index'),

    path(route='about/', view=views.about, name='about'),

    path(route='contact/', view=views.contact, name='contact'),

    path('login/', views.login_request, name='login'),

    path('logout/', views.logout_request, name='logout'),
    path('signup/', views.registration_request, name='signup'),


    # path for contact us view

    # path for registration

    # path for login

    # path for logout


    # path for dealer reviews view

    # path for add a review view

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
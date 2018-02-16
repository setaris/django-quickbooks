from django.conf.urls import url

from . import views

app_name = 'quickbooks'

urlpatterns = (
    url(r'^request_oauth_token/?$',    views.request_oauth_token,  name='request_oauth_token'),
    url(r'^get_access_token/?$',       views.get_access_token,     name='get_access_token'),
    url(r'^blue_dot_menu/?$',          views.blue_dot_menu,        name='blue_dot_menu'),
    url(r'^disconnect/?$',             views.disconnect,           name='disconnect'),
)

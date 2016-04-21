from . import views

urlpatterns = (
    (r'^request_oauth_token/?$',    views.request_oauth_token),
    (r'^get_access_token/?$',       views.get_access_token),
    (r'^blue_dot_menu/?$',          views.blue_dot_menu),
    (r'^disconnect/?$',             views.disconnect),
)


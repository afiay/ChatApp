from django.urls import path, include
from chat import views as chat_views
from django.contrib.auth.views import LoginView, LogoutView
from .views import send_message

urlpatterns = [
    path("", chat_views.chat_page, name="chat-page"),

    # login-section
    path("auth/login/", LoginView.as_view
         (template_name="chat/LoginPage.html"), name="login-user"),
    path("auth/logout/", LogoutView.as_view(), name="logout-user"),
    path('send-message/<int:user_id>/', send_message, name='send_message'),
]

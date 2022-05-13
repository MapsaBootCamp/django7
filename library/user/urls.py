from django.urls import path

from .views import login, logout, SignUp, Login

urlpatterns = [
    path('login/', Login.as_view(), name="login"),
    path('logout/', logout, name="logout"),
    path('signup/', SignUp.as_view(), name="signup"),
]

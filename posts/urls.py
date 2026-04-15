from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path("post/<int:id>/", views.post_detail, name="post"),
    path("form/", views.form, name="form"),
    path("all-data/", views.data, name="data"),
    path("set_cookie/", views.set_cookie_view, name="set_cookie"),
    path("delete_cookie/", views.delete_cookie_view, name="delete_cookie"),
]


from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.loginUser, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("newItem/", views.create_item, name="new"),
    # path('getItems/',views.getItems,name='get'),
    path('item/<int:pk>/', views.item_detail, name='detail'),
    path('myItems/',views.myItems,name='myitems'),
    path('electronics/',views.electronics,name='Electronics'),
    path('fashion/',views.fashion,name='fashion'),
    path('games/',views.games,name='games'),
    path('sports/',views.sports,name='sports'),

]

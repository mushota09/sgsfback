
from user_app.modules.admin_user.views import create_admin ,logout, login_admin,admin_userAPIView,change_password_admin

from user_app.modules.admin_profil_user.views import admin_profilAPIView

from django.urls import path,re_path
from rest_framework import routers

router=routers.DefaultRouter()
router.register("admin_profil",admin_profilAPIView)
router.register("admin_user",admin_userAPIView)



urlpatterns = [
   
    path('logout/',logout ),
    path('login_admin/',login_admin ),
    path('create_admin/',create_admin ),
    path('change_password_admin/',change_password_admin ),
]
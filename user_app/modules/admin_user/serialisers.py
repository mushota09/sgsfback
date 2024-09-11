from rest_framework import serializers
from .model import admin_user
from user_app.modules.admin_profil_user.serialisers import admin_profilSerializers

class joint_admin_userSerializers(serializers.ModelSerializer):
    profil_id=admin_profilSerializers()
    class Meta:
        model=admin_user
        fields="__all__"   
        
class insert_admin_userSerializers(serializers.ModelSerializer):
    
    class Meta:
        model=admin_user
        fields="__all__"   
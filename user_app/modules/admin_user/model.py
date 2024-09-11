from django.db import models
from user_app.modules.admin_profil_user.models import admin_profil
class admin_user(models.Model):
    user_id=models.BigAutoField(primary_key=True,db_column='user_id')
    nom=models.CharField(max_length=80, null=False,db_column='nom')
    prenom=models.CharField(max_length=80, null=True,db_column='prenom')
    password=models.CharField(max_length=100,unique=True, null=False,db_column='password')
    email=models.EmailField(max_length=50, null=False,db_column='email')
    telephone1=models.CharField(max_length=30, null=True,db_column='telephone1')
    telephone2=models.CharField(max_length=30, null=True,db_column='telephone2')
    acteur_agricole_id=models.SmallIntegerField(null=True,db_column='acteur_agricole_id')
    profil_id=models.ForeignKey(admin_profil, null=True,on_delete=models.CASCADE,db_column='profil_id')
    is_connected=models.SmallIntegerField(null=True,db_column='is_connected')
    is_active=models.SmallIntegerField(null=True,db_column='is_active')
    user_code=models.EmailField(max_length=50, null=True,db_column='user_code')
    date_insertion=models.DateTimeField(auto_now_add=True,null=True, db_column="date_insertion")
    
    class Meta: 
        # managed=False
        db_table = 'admin_user'
    def __str__(self):
        return self.NOM

 
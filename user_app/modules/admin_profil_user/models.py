from django.db import models

class admin_profil(models.Model):
    profil_id=models.BigAutoField(primary_key=True,db_column='profil_id') 
    profil_descr=models.CharField(max_length=50,null=True,db_column='profil_descr')
    profil_code=models.CharField(max_length=10,null=True,db_column='profil_code')
    class Meta:
        # managed:False
        db_table = 'admin_profil'
    def __str__(self):
        return self.profil_descr 


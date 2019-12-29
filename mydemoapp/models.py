from django.db import models
from django.core.validators import MaxLengthValidator
from django_resized import ResizedImageField
from PIL import Image
# Create your models here.
class Like(models.Model):
    id = models.AutoField(primary_key = True)
    sess_response = models.CharField(max_length=100)
    button_id = models.CharField(max_length=50,default=0)
        # (validators=[MaxLengthValidator(50)])#we can give MaxLengthValidators to validate the length of integer field.
   
class BT_Contact(models.Model):
    Contact_id = models.AutoField(primary_key = True)
    First_Name =  models.CharField(max_length = 50,default='Default_name')
    Last_Name = models.CharField(max_length = 50,default= 'Default_lastname')
    Emailid = models.CharField(max_length= 100 ,default='Default@email.com')
    Message = models.CharField(max_length= 800 ,default= 'No_Message')

class BT_Imageupload(models.Model):
    Image_id = models.AutoField(primary_key= True)
    Image_name = models.CharField(max_length=200,default='Unnamed_Image')
    Image = ResizedImageField(size=[800,800],upload_to='Media/',blank=True,quality=100)
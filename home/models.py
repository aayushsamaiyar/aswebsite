from django.db import models

# Create your models here.

class Contact(models.Model):
    sno = models.AutoField(primary_key = True)
    name = models.CharField("",max_length=30)
    email = models.CharField("",max_length=40)
    phone = models.CharField("",max_length=15)
    content = models.CharField("",max_length=2000)
    timestamp = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.name

class Projectpost(models.Model):
    project_id = models.AutoField(primary_key= True)
    project_name = models.CharField(max_length=60, default='Heading')
    project_desc = models.TextField(max_length=1000, default='project description')
    git_link = models.CharField(max_length=500, default='#')
    project_link = models.CharField(max_length=500, default='#')
    thumbnail = models.ImageField(upload_to='media/images',default='media/images/img_1.jpg')
    
    def __str__(self):
        return self.project_name

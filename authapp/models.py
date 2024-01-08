from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField(null=True)
    phonenumber=models.CharField(max_length=12,null=True)
    description=models.TextField(null=True)

class Enrollment(models.Model):        
    FullName=models.CharField(max_length=25,null=True)
    Email=models.EmailField(null=True)
    Gender=models.CharField(max_length=25,null=True,blank=True)
    PhoneNumber=models.CharField(max_length=12,null=True)
    DOB=models.CharField(max_length=50,null=True)
    SelectMembershipplan=models.CharField(max_length=200,null=True,blank=
                                          True)
    SelectTrainer=models.CharField(max_length=55,null=True,blank=True)
    Reference=models.CharField(max_length=55,null=True)
    Address=models.TextField(null=True)
    paymentStatus=models.CharField(max_length=55,blank=True,null=True)
    Price=models.IntegerField(max_length=55,blank=True,null=True)
    DueDate=models.DateTimeField(blank=True,null=True)
    timeStamp=models.DateTimeField(auto_now_add=True,blank=True,null=True)

class Trainer(models.Model):
    name=models.CharField(max_length=55,null=True)
    gender=models.CharField(max_length=25,null=True)
    phone=models.CharField(max_length=25,null=True)
    salary=models.IntegerField(max_length=25,null=True)
    timeStamp=models.DateTimeField(auto_now_add=True,blank=True,null=True)


class MembershipPlan(models.Model):
    plan=models.CharField(max_length=185)
    price=models.IntegerField(max_length=55)

    
class Gallery(models.Model):
    title=models.CharField(max_length=100)
    img=models.ImageField(upload_to='gallery')
    timeStamp=models.DateTimeField(auto_now_add=True,blank=True)
    pera=models.TextField(max_length=200)

    
class Attendance(models.Model):
    Selectdate=models.DateTimeField(auto_now_add=True)
    phonenumber=models.CharField(max_length=15)
    Login=models.CharField(max_length=200)
    Logout=models.CharField(max_length=200)
    SelectWorkout=models.CharField(max_length=200,null=True)
    TrainedBy=models.CharField(max_length=200,null=True)
     

     
class about(models.Model):
    image=models.ImageField(upload_to='about')
    subtitle=models.TextField(max_length=200)
    name=models.CharField(max_length=100)
    para=models.TextField()
    
class Team(models.Model):
    title=models.CharField(max_length=100)
    img=models.ImageField(upload_to='gallery')
    pera=models.TextField(max_length=200)
    rate=models.CharField(max_length=7)
    
class Service(models.Model):
    title=models.CharField(max_length=100)
    img=models.ImageField(upload_to='service')
    pera=models.TextField(max_length=200)
    
    
class Home_head(models.Model):
    S_title=models.CharField(max_length=200)
   

class Home_welcome(models.Model):
    title=models.CharField(max_length=200)
    subtitle1=models.TextField()
    text1=models.TextField(max_length=300)
    text2=models.TextField(max_length=300)
    subtitle2=models.TextField(max_length=200)
    img=models.ImageField(upload_to='home')
     
     

     
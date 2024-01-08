from django.contrib import admin
from authapp. models import Contact,Enrollment,Trainer,MembershipPlan,Gallery,Attendance,about,Team,Service,Home_head,Home_welcome

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display=('id', 'name', 'email', 'phonenumber', 'description')
    
# class EnrollmentAdmin(admin.ModelAdmin):
#     list_display=('id', 'FullName', 'email', 'Gender', 'PhoneNumber', 'DOB','SelectMembershipplan','SelectTrainer','Reference','Address','paymentStatus','Price','DueDate','timeStamp')
    
class TrainerAdmin(admin.ModelAdmin):
    list_display=('id', 'name', 'gender', 'phone','timeStamp')
    
class MembershipPlanAdmin(admin.ModelAdmin):
    list_display=('id', 'plan', 'price')
    
class GalleryAdmin(admin.ModelAdmin):
    list_display=('id', 'title', 'img', 'timeStamp')
    
    
class AttendanceAdmin(admin.ModelAdmin):
    list_display=('id', 'Selectdate', 'phonenumber', 'Login','Logout','SelectWorkout', 'TrainedBy')

class aboutAdmin(admin.ModelAdmin):
    list_display=('id', 'name', 'subtitle', 'image','para')
    
class TeamAdmin(admin.ModelAdmin):
    list_display=('id', 'title', 'pera', 'rate','img')
    
class ServiceAdmin(admin.ModelAdmin):
    list_display=('id', 'title', 'pera','img')
    
class Home_headAdmin(admin.ModelAdmin):
    list_display=('id','S_title')
    
class Home_welcomeAdmin(admin.ModelAdmin):
    list_display=('id', 'title', 'subtitle1', 'text1','text2','subtitle2', 'img')


admin.site.register(Contact,ContactAdmin)
admin.site.register(Enrollment)
admin.site.register(Trainer,TrainerAdmin)
admin.site.register(MembershipPlan,MembershipPlanAdmin)
admin.site.register(Gallery,GalleryAdmin)
admin.site.register(Attendance,AttendanceAdmin)
admin.site.register(about,aboutAdmin)
admin.site.register(Team,TeamAdmin)
admin.site.register(Service,ServiceAdmin)
admin.site.register(Home_head,Home_headAdmin)
admin.site.register(Home_welcome,Home_welcomeAdmin)
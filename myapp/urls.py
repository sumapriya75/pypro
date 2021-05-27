from django.urls import path
from myapp import views
app_name="myapp"

urlpatterns=[
    path('index/',views.index,name="index"),
    path('courses/',views.courses,name="courses"),
    path('aboutus/',views.aboutus,name="aboutus"),
    path('enquiry/',views.enquiry,name="enquiry"),
]
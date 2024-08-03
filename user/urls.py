from django.urls import path
from . import views
urlpatterns=[
 #   path('admin/', admin.site.urls),
    path('index/',views.index),
    path('',views.index),
    path('vision/',views.vision),
    path('stories/',views.stories),
    path('volunteers/',views.ourvolunteers),
    path('upcommingevent/',views.upcomingevent),
    path('need/',views.need),
    path('donate/',views.donateus),
    path('login/',views.login),
    path('contact/',views.contact),
    path('viewevent/',views.viewevent),
    path('volunteerlist/',views.volunteerlist),

]
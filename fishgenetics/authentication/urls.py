from django.conf import settings
from django.contrib import admin
from django.urls import path ,include
from django.conf.urls.static import static
from authentication import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name="home"),
    path('signup', views.signup,name="signup"),
    path('signin',views.signin,name="signin"),
    path('signout',views.signout,name="signout"),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),

     path('fishgens',views.fishgen, name="fishgen"),


    path('habitatparameter',views.habitparameter , name="habit"),
    path('checkshow',views.checkshow,name="habshow"),

    path('resources',views.forms,name="forms"),
    path('showdata',views.showdata,name="formshow"),
    path('showdata', views.updateform_data, name="updateform"),


    path('fishbiodiversityprimary',views.fishprimary,name="fishprimary"),
    path('fishshow',views.showfish,name="fishshow"),

    path('fishsec',views.fishsec,name="fishsec"),
    path('fishdata',views.fishdata,name="fishshow"),

    path('exoticfish',views.exoticfish,name="fishsec"),
    path('fishdata',views.fishdata,name="fishshow"),



] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
 
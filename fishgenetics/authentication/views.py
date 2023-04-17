from importlib import resources
import profile
from django.shortcuts import render

# Create your views here.
from tokenize import generate_tokens
from urllib import request
from django.conf import settings
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
#from authentication import settings
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth import authenticate, login, logout

from .forms import     Fishbiodiversity_primaryRegistration, FishbiodiversitysecRegistration, FishbioforexoticfishRegistration, FormsRegistration, HabitatparameterRegistration
from .models import   fishbiodiversity_primary, fishbiodiversitysec, fishbioforexoticfish, form, habitatparameter 
from . tokens import generate_token






# Create your views here.
def home(request):
    return render(request, "authentication/index.html")

def signup(request):

        if request.method == "POST":
            username = request.POST['username']
            fname = request.POST['fname']
            lname = request.POST['lname']
            email = request.POST['email']
            pass1 = request.POST['pass1']
            pass2 = request.POST['pass2']


            if User.objects.filter(username=username):
                messages.error(request, "Username already exist! Please try some other username")
                return redirect('home')
            
            if User.objects.filter(email=email):
                messages.error(request, "Email already registered!")
            
            if len(username)>10:
                messages.error(request, "Username must be under 10 characters")
            
            if pass1!=pass2:
                messages.error(request, "Passwords didn't match!")

            if not username.isalnum():
                messages.error(request, "Username must be Alpha-Numeric!")
                return redirect('home')
            



            myuser = User.objects.create_user(username,email,pass1)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.is_active = False

            myuser.save()

            messages.success(request, "Your Account has been successfully created. We have sent you a confirmation email, please confirm your email in order to activate your account")


            # Welcome Email

            subject = "Welcome to ICAR - Login!!"
            message = "Hello " + myuser.first_name + "!!\n"+"Welcome to ICAR!! \n Thankyou for visiting our website \n We have also sent you a confirmation email, please confirm your email address in order to activate your account.\n\n Thanking You \n Charul Pathak"
            from_email = settings.EMAIL_HOST_USER
            to_list = [myuser.email]
            send_mail(subject,message, from_email, to_list, fail_silently=True)


            # Email Address Confirmation Email

            current_site = get_current_site(request)
            email_subject = "Confirm your Email @ ICAR --LOGIN!!"
            message2 = render_to_string('email_confirmation.html',{

                'name': myuser.first_name,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
                'token': generate_token.make_token(myuser)
            })
            email = EmailMessage(
                email_subject,
                message2,
                settings.EMAIL_HOST_USER,
                [myuser.email],
            )
            email.fail_silently = True
            email.send()


            return redirect('signin')


        return render(request, "authentication/signup.html")


def activate(request,uidb64,token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError,ValueError,OverflowError,User.DoesNotExist):
        myuser = None
    
    if myuser is not None and generate_token.check_token(myuser,token):
        myuser.is_active = True
        # user.profile.signup_confirmation = True
        myuser.save()
        login(request,myuser)
        messages.success(request, "Your Account has been activated!!")
        return redirect('home')
    else:
        return render(request,'activation_failed.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            fname = user.first_name
            # messages.success(request, "Logged In Sucessfully!!")
            return render(request, "authentication/fishgen.html",{"fname":fname})
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('home')
    
    return render(request, "authentication/signin.html")


def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('home')






def fishgen(request):
    return render(request,"authentication/fishgen.html")   




def habitparameter(request):
    if request.method == 'POST':
        fm = HabitatparameterRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            fm = HabitatparameterRegistration()
    else:
        fm = HabitatparameterRegistration()
    fd = habitatparameter.objects.all()
    return render(request,'authentication/habitatparameter.html',{'form':fm, 'fdd':fd})       


def checkshow(request):
    sh = habitatparameter.objects.all()
    return render(request,'authentication/habitshow.html', {'fr':sh})     



def forms(request):
    if request.method == 'POST':
        rs = FormsRegistration(request.POST)
        if rs.is_valid():
            rs.save()
            rs = FormsRegistration()
    else:
        rs= FormsRegistration()
    fs = form.objects.all()
    return render(request,'authentication/form.html',{'form':rs, 'fso':fs})       


def showdata(request):
    sho = form.objects.all()
    return render(request,'authentication/formshow.html', {'fr': sho})

def updateform_data(request, id):
    if request.method == 'POST':
        rs = form.objects.get(pk=id)
        rs = FormsRegistration(request.POST, instance=checkprod)
        if rs.is_valid():
            rs.save()
    else:
        checkprod = form.objects.get(pk=id)
        rs = FormsRegistration(instance=checkprod)
    return render(request, 'authentication/updateform.html',{'form':rs})



def  fishprimary(request):
    if request.method == 'POST':
        rsi = Fishbiodiversity_primaryRegistration(request.POST)
        if rsi.is_valid():
            rsi.save()
            rsi = Fishbiodiversity_primaryRegistration()
    else:
        rsi= Fishbiodiversity_primaryRegistration()
    fsi = fishbiodiversity_primary.objects.all()
    return render(request,'authentication/fishprimary.html',{'form':rsi})

def showfish(request):
    shf = fishbiodiversity_primary.objects.all()
    return render(request,'authentication/fishprimaryshow.html', {'fr':shf}) 





def  fishsec(request):
    if request.method == 'POST':
        rsi = FishbiodiversitysecRegistration(request.POST)
        if rsi.is_valid():
            rsi.save()
            rsi = FishbiodiversitysecRegistration()
    else:
        rsi= FishbiodiversitysecRegistration()
    fsi = fishbiodiversitysec.objects.all()
    return render(request,'authentication/fishsecdata.html',{'form':rsi})


def fishdata(request):
    shf = fishbiodiversitysec.objects.all()
    return render(request,'authentication/fishsecshow.html', {'fr':shf}) 



def exoticfish(request):
    if request.method == 'POST':
        fm = FishbioforexoticfishRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            fm = FishbioforexoticfishRegistration()
    else:
        fm = FishbioforexoticfishRegistration()
    fd = fishbioforexoticfish.objects.all()
    return render(request,'authentication/exoticfish.html',{'form':fm, 'fdd':fd}) 




 







     

  



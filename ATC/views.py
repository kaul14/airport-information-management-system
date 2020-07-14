from django.shortcuts import render,redirect,render_to_response
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings
from . models import NewArrivalModel,NewDepartureModel
from . forms import AircraftTypeForm,NewLocationForm,NewwOperatorForm,NewAircraftForm,NewDepartureForm,NewArrivalForm







def LoginView(request):

    return render(request,'registration/login.html')

    #username = request.POST['username']
    #password = request.POST['password']
    #user = authenticate(request, username=username, password=password)
    #if user is not None:
    #    login(request,'base.html')
        # Redirect to a success page.
    #    ...
    #else:
        # Return an 'invalid login' error message.
    #    ...

def HomeView(request):
    subject='LOGIN ALERT'
    message='NEW USER HAS LOGGED IN AIMS WEBSITE , PLEASE CHECK AUTHENTICAION '
    from_email=settings.EMAIL_HOST_USER
    to_list=['bhaviyabatra0912@gmail.com']
    #send_mail(subject,message , from_email,to_list,fail_silently=True)
    return render(request,'base.html')

def OperatorView(request):
    if request.method == "POST":
        form= NewwOperatorForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('ATC:new_operator')
        else:
            print(form.errors)
    else:
        form=NewwOperatorForm()
    return render(request,'newoperator.html', {'form': form})


def AircraftTypeView(request):
    if request.method == "POST":
        form= AircraftTypeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('ATC:aircraft_type')
        else:
            print(form.errors)

    else:
        form=AircraftTypeForm()
    return render(request,'aircraft_type.html', {'form': form})

def LocationView(request):
    if request.method == "POST":
        form= NewLocationForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('ATC:location')
        else:
            print(form.errors)
    else:
        form=NewLocationForm()
    return render(request,'location.html', {'form': form})



def AircraftNewView(request):
    if request.method == "POST":
        form= NewAircraftForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('ATC:aircraft_new')
        else:
            print(form.errors)

    else:
        form=NewAircraftForm()
    return render(request,'new_aircraft.html', {'form': form})

def ScheduleView(request):
    return render(request,'schedule_flight.html')

def ScheduleDepartureView(request):
    if request.method == "POST":
        form= NewDepartureForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('ATC:schedule_departure')
        else:
            print(form.errors)
    else:
        form=NewDepartureForm()
    return render(request,'departure_flight.html', {'form': form})

def ScheduleArrivalView(request):
    if request.method == "POST":
        form= NewArrivalForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('ATC:schedule_arrival')
        else:
            print(form.errors)
    else:
        form=NewArrivalForm()
    return render(request,'arrival_flight.html', {'form': form})

def DisplayView(request):
    dataone=NewDepartureModel.objects.all()
    data = NewArrivalModel.objects.all()
    arrival = {
    "data": data,'dataone':dataone
}
    return render_to_response('display.html', arrival)






# Create your views here.

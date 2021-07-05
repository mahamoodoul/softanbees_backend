from django.shortcuts import render
from .models import ApplyModel, EmailModel
from django.http import JsonResponse
# Create your views here.

def home(request):
    template_name = 'home.html'
    return render(request,template_name)

def send_info(request):
    if request.method == 'POST' and request.is_ajax:
        email = request.POST.get('email')
        if ApplyModel.objects.filter(email=email).exists():
            request.session['email'] = email
            email = request.POST.get('email')
            # message = 'Email already exsists !!'
            message = 'exist'
        else:
            name = request.POST.get('name')
            profession = request.POST.get('toggle')
            create_apply_object = ApplyModel.objects.create(name=name,email=email,profession=profession)
            create_apply_object.save()
            request.session['email'] = email
            # message = "Your Account Created Successfully"
            message = "success"
        return JsonResponse({"message": message}, status=200)

def send_email(request):
    if request.method == 'POST' and request.is_ajax:
        email = request.POST.get('email')
        if EmailModel.objects.filter(only_email=email).exists():
            request.session['email'] = email
            message = 'Email already exsists !!'
        else:
            create_emial_object = EmailModel.objects.create(only_email=email)
            create_emial_object.save()
            request.session['email'] = email
            message = "Your Account Created Successfully"
        return JsonResponse({"message": message}, status=200)


def CourseDetails(request):
    template_name = 'course_details/details.html'
    return render(request,template_name)
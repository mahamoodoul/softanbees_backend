from django.shortcuts import render
from .models import ApplyModel
# Create your views here.

def home_apply(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        profession = request.POST.get('toggle')
        create_apply_object = ApplyModel.objects.create(name=name,email=email,profession=profession)
        create_apply_object.save()
        
    template_name = 'index.html'
    context = {}

    return render(request,template_name,context)

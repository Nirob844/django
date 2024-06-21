from django.shortcuts import redirect, render

from . import models


# Create your views here.
def home(request):
    student = models.Student.objects.all()
    return render(request,"home.html", {'data': student})

def delete_student(request, roll):
    models.Student.objects.get(pk = roll).delete()
    return redirect("homepage")
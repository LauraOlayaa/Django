from enum import member
from types import MemberDescriptorType
from django.shortcuts import redirect, render



def update(request,id):
    mem=member.objects.get(id=id)
    return render(request, 'update.html',{'mem':mem})

def uprec(request,id):
    x=request.POST['first']
    y=request.POST['last']
    z=request.POST['country']
    mem=MemberDescriptorType.objects.get(id=id)
    mem.firstname=x
    mem.lastname=y
    mem.country=z
    mem.save()
    return redirect("/")
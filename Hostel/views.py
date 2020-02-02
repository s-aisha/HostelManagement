
from rest_framework import generics
from  .models import Entry
from .serializers import EntrySerializers
from django.shortcuts import render,redirect

from django.core.mail import send_mail
from django.conf import settings




class EntriesList(generics.ListCreateAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializers



def home(request):
    return render(request,'index.html')


def add(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        place = request.POST.get('place', '')
        reason = request.POST.get('reason', '')
        return_date = request.POST.get('reentry', '')
        degree = request.POST.get('degree', '')
        branch = request.POST.get('branch', '')
        year = request.POST.get('year', '')
        block_name = request.POST.get('block', '')
        par_email = request.POST.get('email', '')
        room_no = request.POST.get('room', '')
        rt_name = request.POST.get('rt', '')
        check_with = request.POST.get('check', '')
        pass_available = request.POST.get('pass', '')

        obj = Entry(name=name,place=place,reason=reason,return_date=return_date,degree=degree,branch=branch,year=year,
                    block_name=block_name,room_no=room_no,rt_name=rt_name,check_with=check_with,pass_available=pass_available)
        if  obj.save() is None:
           
            res  =  0
            try :
                res =send_mail(
                    'TBAK Hostel',
                    'Dear Parents,\n You daughter {0} \nstudying {1} {2} {3} year \nhas left the hostel due to '
                    '{4} to {5} and mentioned return time is {6} RT name is {7} contact Rt for more information'
                        .format(name,degree,branch,year,reason,place,return_date,rt_name),
                    settings.EMAIL_HOST_USER,
                    [par_email,],
                    fail_silently=False
                )
                
                return redirect('/home?saved=True')
            except Exception as e :
                print(res)
                print(e)
        else :            
            return redirect('/home?error=True')
    return render(request,'index.html')

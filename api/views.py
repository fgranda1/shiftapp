from operator import length_hint
from django.db.models import manager
from django.shortcuts import render
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from main.models import *


#login
from django.contrib.auth import authenticate, login, logout

#date
import dateutil.parser
from datetime import date, datetime, timedelta, time


#Utils
import csv
import pandas as pd
import os

#Json
from django.http import JsonResponse
import json


# Create your views here.

  
   

def get_shift(request):

    

    #Getting from to
    #Getting Shift Model
    shift =  Shift.objects.filter(shift_person__msid = 'lriver75')

    shift_list = []
    for s in shift:
        shift_list.append(s)
    
    #List of time ranges
    shift_time_range_list = []   

    shift_id_list = []

    

    for sl in shift_list:             
        shift_id_list.append(sl.shift_id)        
        
        date = sl.date
        #Converting into a dict

        


        for i in sl.sch_time_range.all():
            shift_time_range_list.append(
                {   
                    'shift_id': [sid for sid in shift_id_list ][-1],
                    'date': date.strftime("%m-%d-%Y"),                    
                    'sch_from': i.sch_from.strftime("%H:%M:%S"),
                    'sch_to':i.sch_to.strftime("%H:%M:%S"),
                    'length': int((datetime.combine(date.today(), i.sch_to) - datetime.combine(date.today(), i.sch_from)).seconds / 60 ),
                    'sch_activity':i.sch_activity.act,
                }
            )  

   
    final = []
    
    for i in [s for s in shift_id_list]:
        
        activity = []
        

        for f in shift_time_range_list:
            if f['shift_id'] == i:
                activity.append(
                    
                    {                  
                    'sch_from': f['sch_from'],
                    'sch_to': f['sch_to'],
                    'sch_activity': f['sch_activity'],
                    'length': f['length']
                                
                    }
                )


                data = {
                    'date': f['date'],                    
                    'shift_id': f['shift_id'],
                    'activity': activity,
                }
        

                if data in final:
                    pass
                else:
                    final.append(data)     
    

    
    return JsonResponse(status=200, data=final, safe=False)



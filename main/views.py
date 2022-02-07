from operator import length_hint
from django.db.models import manager
from django.shortcuts import render
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *


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
  

def index(request):    
    return render(request, 'main/index.html'  )



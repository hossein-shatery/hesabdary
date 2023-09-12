from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from json import JSONEncoder
from kh_d.models import kharj,User,token,dakhl
from datetime import datetime

@csrf_exempt
def defkharj(request):
   token = request.POST['token']
   adad = request.POST['adad']
   text = request.POST['text']
   user = User.objects.filter(token__token = token).get()
   if 'date' not in request.POST:
      date = datetime.now()
   kharj.objects.create(user=user , adad = adad , text = text , date=date , )
   print ('man ezafe shodam')
   print (request.POST)
   
   return JsonResponse({
       'status' : 'ok',},
        encoder=JSONEncoder)

@csrf_exempt
def defdakhl(request):
   token = request.POST['token']
   adad = request.POST['adad']
   text = request.POST['text']
   user = User.objects.filter(token__token = token).get()
   if 'date' not in request.POST:
      date = datetime.now()
   dakhl.objects.create(user=user , adad = adad , text = text , date=date , )
   print ('man ezafe shodam')
   print (request.POST)
   
   return JsonResponse({
       'status' : 'ok',},
        encoder=JSONEncoder)        

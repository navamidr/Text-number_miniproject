from django.shortcuts import render
from django.http import JsonResponse
from .models import conversion
# from .models import Conversion
from .models import Convert
from word2number import w2n
import json

# Create your views here.
# def hello(request):
#     return HttpResponse("hello")

def print(request):
    return render(request,'index.html')

def convert(request):
    if request.method == "POST":
        data = json.loads(request.body)
        text= data.get('text','').strip()
        if not text:
            return JsonResponse({"error":"input cannot be empty"},status=400)
        
        try:
            result=w2n.word_to_num(text)
            conversions=Convert.objects.create(text_input=text,number_result=result)
            return JsonResponse({"result":result})
        except ValueError:
            return JsonResponse({"error":"invalid input"},status=400)
        
    return JsonResponse({"error":"invalid mathod"},status=405)
    




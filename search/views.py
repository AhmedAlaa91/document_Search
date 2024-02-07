from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from django.http import HttpResponse
from django.http import JsonResponse
import json
from urllib.parse import unquote

from .utils import search
# Create your views here.
import requests

class Documents():
    


    @api_view(('POST',))
    def get_documents(request):
        documents=search.retrive_documents()
       
        data = request.body
        data = str(data, encoding='utf-8')
        data = unquote(data)
        data = json.loads(data)
        query = data['query']

        result = search.semantic_search(query, documents, 'Multiple')
        result=json.loads(json.dumps(str(result).strip()))
     
        return HttpResponse(result)
    

    
    @api_view(('POST',))
    def get_single_document(request):
        documents=search.retrive_documents()
       
        data = request.body
        data = str(data, encoding='utf-8')
        data = unquote(data)
        data = json.loads(data)
        query = data['query']


        test="{'Document 1': 'Python is a versatile language.'}"

        result = search.semantic_search(query, documents, 'Single')
        result=json.dumps(str(result).strip())
     
        return HttpResponse(result.replace('"',' '))
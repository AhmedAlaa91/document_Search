from django.urls import path
from .views import Documents


urlpatterns = [
    path('get-documents', Documents.get_documents),
    path('get-single-document', Documents.get_single_document),

]
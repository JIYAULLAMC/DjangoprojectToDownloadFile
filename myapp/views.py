from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

app_name = "myapp"

def home(request):
    return render(request, "myapp/home.html")

from django.http import StreamingHttpResponse
from wsgiref.util import FileWrapper
import os

def download(request):
   curent_dir = os.getcwd()
   current_folder = "myapp"
   file_path = f"{curent_dir}\{current_folder}"
   filename = "\car6.jpg"
   file_path += filename
   chunk_size = 8192
   response = StreamingHttpResponse(
       FileWrapper(open(file_path, 'rb'), chunk_size),
       content_type="application/octet-stream"
   )
   response['Content-Length'] = os.path.getsize(file_path)    
   response['Content-Disposition'] = "attachment; filename=%s" % filename
   return response

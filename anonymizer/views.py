from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

# Create your views here.
def view_file(request):
	 return render(request, 'view_file.html')
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
#from .models import Upload
#from uploads.core.models import Document
from .forms import DocumentForm

# Create your views here.
def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            #if user.is_authenticated():
               #user_id=user.pk
            form.save()
            return redirect('login')
    else:
        form = DocumentForm()
    return render(request, 'form/model_form_upload.html', {'form': form})

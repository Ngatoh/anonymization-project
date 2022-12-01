from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

# Create your views here.
def view_file(request):
	 return render(request, 'view_file.html')

def add_view(request):
        form = PostForm()
        return render(request, 'admin/anonymizer/add_form.html', {'form': form})
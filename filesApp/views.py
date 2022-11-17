from django.shortcuts import render
from .models import Files
from .forms import FilesForm
from django.contrib import messages
# Create your views here.

def upload(request):
	if request.method=='POST':
		form = FilesForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, 'Files uploaded')
	form = FilesForm()
	return render(request,'upload_file.html',{'form':form})

def download(request):
	files=Files.objects.all()
	return render(request,'download_file.html',{'files':files})


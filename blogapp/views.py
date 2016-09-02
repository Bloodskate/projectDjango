from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import BlogPost
from .forms import BlogPostForm
# Create your views here.
def homepage(request):
	blogs=BlogPost.objects.all()
	context ={'nabin':blogs}
	template_name='index.html'
	return render(request,template_name,context)
	#return HttpResponse('<h1>hello nabin kharal</h1>')	
def details(request,pk):
	template_name='details.html'
	blog=BlogPost.objects.get(pk=pk)
	return render(request,template_name,{'blog':blog})

def newblog(request):
	if request.method =='POST':
		form = BlogPostForm(request.POST)
		if form.is_valid():
			post=form.save(commit=False)
			post.save()
			return redirect('blogapp.views.details',pk=post.pk)
	else:
		form=BlogPostForm()
	return render(request,'newblog.html',{'form':form})
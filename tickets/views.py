from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from . import forms



@login_required
def blog_and_photo_upload(request):
    blog_form = forms.BlogForm()
    photo_form = forms.PhotoForm()
    if request.method == 'POST':
        blog_form = forms.BlogForm(request.POST)
        photo_form = forms.PhotoForm(request.POST, request.FILES)
        if any ([blog_form.is_valid(), photo_form.is_valid()]):
            photo = photo_form.save(commit=False)
            photo_upload = request.user
            photo.save()
            
            blog = blog_form.save(commit=False)
            blog.author = request.user
            blog.photo = photo
            blog.save()
            return redirect('blog')
    context = {
        'blog_form': blog_form,
        'photo_form': photo_form,
        }
    return render(request, 'tickets/tickets.html', context=context)

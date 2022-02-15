from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from . import forms


@login_required
def criticize(request):
    bookArticle_form = forms.BookArticleForm()
    criticize_form = forms.CriticizeForm()
    photo_form = forms.PhotoForm()
    if request.method == 'POST':
        bookArticle_form = forms.BookArticleForm(request.POST)
        criticize_form = forms.CriticizeForm(request.POST)
        photo_form = forms.PhotoForm(request.POST, request.FILES)
        if any ([bookArticle_form.is_valid(), photo_form.is_valid()]):
            photo = photo_form.save(commit=False)
            photo_upload = request.user
            photo.save()
            
            bookArticle = bookArticle_form.save(commit=False)
            bookArticle.author = request.user
            bookArticle.photo = photo
            bookArticle.save()
            
            criticize = criticize_form.save(commit=False)
            criticize.author = request.user
            criticize.save()
            return redirect('blog')
    context = {
        'bookArticle_form': bookArticle_form,
        'criticize_form': criticize_form,
        'photo_form': photo_form,
        }
    return render(request, 'criticize/criticize.html', context=context)

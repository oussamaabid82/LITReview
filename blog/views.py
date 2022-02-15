<<<<<<< HEAD
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required

def display(request):
    return render(request, 'blog/flux.html')
=======
from itertools import chain

from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import TicketForm, DeleteReviewForm, FollowUsersForm, ReviewForm
from .models import Review, Ticket



@login_required
def home(request):
    review = Review.objects.filter(
        Q(contributors__in=request.user.follows.all()) | Q(starred=True))
    
    # ticket = Ticket.objects.filter(Q(contrib__in=request.user.follows.all())) 
    
    # photos = Photo.objects.filter(
    #     uploader__in=request.user.follows.all())

    review_and_ticket = sorted(
        chain(review),
        key=lambda instance: instance.date_created,
        reverse=True
    )
    paginator = Paginator(review_and_ticket, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}

    return render(request, 'blog/home.html', context=context)

@login_required
def create_ticket(request):
    ticket_form = TicketForm()
    if request.method == 'POST':
        ticket_form = TicketForm(request.POST)
        if all ([ticket_form.is_valid()]):
            ticket = Ticket()
            ticket.title = request.POST['title']
            ticket.description = request.POST['description']            
            ticket.save()
            ticket.contrib.add(request.user)
            return redirect('home')
    context = {
        'ticket_form': ticket_form,
        }
    return render(request, 'blog/tickets.html', context=context)


@login_required
def create_review(request):
    blog_form = ReviewForm()
    if request.method == 'POST':
        blog_form = ReviewForm(request.POST)
        if all([blog_form.is_valid()]):
           
            blog = Review()
            blog.title = request.POST['title']
            blog.content = request.POST['commentaire']
            blog.rating = request.POST['rating']
            blog.author = request.user
            blog.save()
            blog.contributors.add(request.user, through_defaults={'contribution': 'Auteur principal'})
            return redirect('home')
    context = {
        'blog_form': blog_form,
    }
    return render(request, 'blog/create_review.html', context=context)

@login_required
def view_blog(request, blog_id):
    blog = get_object_or_404(Review, id=blog_id)
    return render(request, 'blog/view_review.html', {'blog': blog})


@login_required
def edit_blog(request, blog_id):
    blog = get_object_or_404(Review, id=blog_id)
    edit_form = ReviewForm()
    delete_form = DeleteReviewForm()
    if request.method == 'POST':
        if 'edit_blog' in request.POST:
            edit_form = ReviewForm(request.POST, instance=blog)
            if all ([edit_form.is_valid()]):
                
                edit_form.save()
                
                return redirect('home')
        if 'delete_blog' in request.POST:
            delete_form = DeleteReviewForm(request.POST)
            if delete_form.is_valid():
                blog.delete()
                return redirect('home')
    context = {
        'edit_form': edit_form,
        'delete_form': delete_form,
    }
    return render(request, 'blog/edit_blog.html', context=context)


@login_required
def follow_users(request):
    form = FollowUsersForm(instance=request.user)
    if request.method == 'POST':
        form = FollowUsersForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'blog/follow_users_form.html', context={'form': form})


def photo_feed(request):
    paginator = Paginator( 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'blog/photo_feed.html', context=context)
>>>>>>> 988f8af (MAJ programme)

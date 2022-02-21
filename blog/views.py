from django.db.models import Q
from itertools import chain
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from .forms import TicketForm, DeleteReviewForm, FollowUsersForm, ReviewForm
from .models import Review, Ticket



@login_required
def home(request):
    
    ticket = Ticket.objects.filter(
        Q(user__in = request.user.follows.all()) | Q(user=True))
    
    review = Review.objects.filter(
        Q(user__in = request.user.follows.all()) | Q(user=True))
        
    review_and_ticket = sorted(
        chain(review, ticket),
        key=lambda instance: instance.date_created,
        reverse=True
    )
  
    paginator = Paginator(review_and_ticket, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'ticket': ticket,
        'review': review
        }
    
    return render(request, 'blog/home.html', context=context)

@login_required
def create_ticket(request):
    if request.method == 'POST':
        ticket_form = TicketForm(request.POST, request.FILES)
        if ticket_form.is_valid():
            ticket = Ticket()
            ticket.title = ticket_form.cleaned_data['title']
            ticket.description = ticket_form.cleaned_data['description']
            ticket.image = ticket_form.cleaned_data['image']
            ticket.user = request.user  
            ticket.save()
            # ticket.contributors.add(request.user, through_defaults={'ticket_contributions': 'Auteur principal'})

            return redirect('home')
    else:
        ticket_form = TicketForm()
        
    context = {
        'ticket_form': ticket_form,
        }
    return render(request, 'blog/tickets.html', context=context)


@login_required
def create_review(request):
    if request.method == 'POST':
        ticket_form = TicketForm(request.POST, request.FILES)
        review_form = ReviewForm(request.POST)
        if all([ticket_form.is_valid(), review_form.is_valid()]):
            ticket = Ticket()
            ticket.title = ticket_form.cleaned_data['title']
            ticket.description = ticket_form.cleaned_data['description']
            ticket.image = ticket_form.cleaned_data['image']
            ticket.user = request.user  
            ticket.save()
            # ticket.contributors.add(request.user, through_defaults={'ticket_contributions': 'Auteur principal'})
            
            review = Review()
            review.ticket = ticket
            review.title = request.POST['title']
            review.content = request.POST['commentaire']
            review.rating = request.POST['rating']
            review.user = request.user
            review.save()
            # review.contributors.add(request.user, through_defaults={'review_contributions': 'Auteur principal'})
            return redirect('home')
    else:
        ticket_form = TicketForm()
        review_form = ReviewForm()
        
    context = {
        'ticket_form': ticket_form,
        'review_form': review_form,
    }
    return render(request, 'blog/create_review.html', context=context)

@login_required
def view_blog(request, blog_id):
    blog = get_object_or_404(Review, id=blog_id)

    return render(request, 'blog/view_review.html', {'blog': blog})

@login_required
def edit_blog(request, blog_id):
    blog = get_object_or_404(Review, id=blog_id)
    edit_review = ReviewForm(request.POST, blog)
    
    if request.method == 'POST':
        if 'edit_review' in request.POST:
            edit_review = ReviewForm(request.POST, instance=blog)
            if edit_review.is_valid():
                edit_review.save()
                return redirect('home')
            
        if 'delete_blog' in request.POST:
            delete_review = DeleteReviewForm(request.POST)
            if delete_review.is_valid():
                blog.delete()
                return redirect('home')
    else:
        edit_review = ReviewForm()
        delete_review = DeleteReviewForm()
        
    context = {
        'edit_review': edit_review,
        'delete_review': delete_review,
    }
    return render(request, 'blog/edit_blog.html', context=context)


@login_required
def follow_users(request):
    form = FollowUsersForm(instance=request.user)
    if request.method == 'POST':
        form = FollowUsersForm(request.POST, instance=request.user)
        if form.is_valid():
            # django forms initial values
            form.save()
            return redirect('home')
    return render(request, 'blog/follow_users_form.html', context={'form': form})


# def photo_feed(request):
#     paginator = Paginator( 10)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     context = {'page_obj': page_obj}
#     return render(request, 'blog/photo_feed.html', context=context)

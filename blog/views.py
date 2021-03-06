from django.db.models import Q
from itertools import chain
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from authentication.models import UserFollows
from .forms import TicketForm, ReviewForm, SearchUserForm
from .models import Review, Ticket


@login_required
def home(request):
    ticket = Ticket.objects.filter(Q(user__in=request.user.follows.all()) | Q(user=request.user))
    review = Review.objects.filter(Q(user__in=request.user.follows.all()) | Q(user=request.user))

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

        }
    return render(request, 'blog/home.html', context=context)


@login_required
def post(request):
    ticket = Ticket.objects.filter(user=request.user)
    review = Review.objects.filter(user=request.user)
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
        }
    return render(request, 'blog/post.html', context=context)


@login_required
def create_ticket(request):
    if request.method == 'POST':
        ticket_form = TicketForm(request.POST, request.FILES)
        if ticket_form.is_valid():
            ticket = Ticket()
            ticket.title_ticket = ticket_form.cleaned_data['title_ticket']
            ticket.description = ticket_form.cleaned_data['description']
            ticket.image = ticket_form.cleaned_data['image']
            ticket.user = request.user
            ticket.save()
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
            ticket.title_ticket = ticket_form.cleaned_data['title_ticket']
            ticket.description = ticket_form.cleaned_data['description']
            ticket.image = ticket_form.cleaned_data['image']
            ticket.user = request.user
            ticket.save()
            review = Review()
            review.ticket = ticket
            review.title_review = request.POST['title_review']
            review.content = request.POST['content']
            review.rating = request.POST['rating']
            review.user = request.user
            review.save()
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
def create_review_response_ticket(request, blog_id):
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        ticket = get_object_or_404(Ticket, id=blog_id)
        if review_form.is_valid():
            review = Review()
            review.ticket = ticket
            review.title_review = request.POST['title_review']
            review.content = request.POST['content']
            review.rating = request.POST['rating']
            review.user = request.user
            review.save()
            return redirect('home')
    else:
        review_form = ReviewForm()
        ticket = get_object_or_404(Ticket, id=blog_id)

    context = {
        'review_form': review_form,
        'ticket': ticket,
    }
    return render(request, 'blog/create_review_response.html', context=context)


@login_required
def view_blog(request, blog_id):
    blog = get_object_or_404(Review, id=blog_id)

    return render(request, 'blog/view_review.html', {'blog': blog})


@login_required
def edit_review(request, blog_id):
    blog = get_object_or_404(Review, id=blog_id)
    if request.method == 'POST':
        edit_review = ReviewForm(request.POST, instance=blog)
        if edit_review.is_valid():
            edit_review.save()
            return redirect('post')
    else:
        edit_review = ReviewForm(instance=blog)
    context = {
        'edit_review': edit_review,
        'review': blog,
    }
    return render(request, 'blog/edit_review.html', context=context)


@login_required
def edit_ticket(request, blog_id):
    ticket = get_object_or_404(Ticket, id=blog_id)
    if request.method == 'POST':
        edit_ticket = TicketForm(request.POST, request.FILES, instance=ticket)
        if edit_ticket.is_valid():
            edit_ticket.save()
            return redirect('post')
    else:
        edit_ticket = TicketForm(instance=ticket)
    context = {
        'edit_ticket': edit_ticket,
    }
    return render(request, 'blog/edit_ticket.html', context=context)


@login_required
def delete_review(request, blog_id):
    review = get_object_or_404(Review, id=blog_id)
    review.delete()
    return redirect('post')


@login_required
def delete_ticket(request, blog_id):
    ticket = get_object_or_404(Ticket, id=blog_id)
    ticket.delete()
    return redirect('post')


@login_required
def follow_users(request):
    following = []
    follows = []
    message = ''
    user = request.user
    if request.method == 'POST':
        form = SearchUserForm(request.POST)
        username = request.POST['username']
        # verifier si username est un utilisateur
        try:
            searched_user = UserFollows.objects.get(username=username)
            if searched_user != user:
                user.follows.add(searched_user)
            follows = user.follows.all()
        except UserFollows.DoesNotExist:
            follows = user.follows.all()
            message = ("utilisateur inexistant")
    else:
        form = SearchUserForm()
        follows = user.follows.all()
        message = ''
    follow = UserFollows.objects.all()
    for follow in follow:
        list_users = follow.follows.all()
        if user in list_users:
            following.append(follow)
    context = {
        'form': form,
        'follows': follows,
        'following': following,
        'message': message
    }
    return render(request, 'blog/follow_users_form.html', context=context)


@login_required
def unfollow_follow_users(request, follows_id):
    user = request.user
    user.follows.remove(follows_id)
    return redirect('follow_users')

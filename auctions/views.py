from ast import Not
from operator import is_
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import User, Listing, Category

from .forms import *
from .models import *



def index(request):
    listings = Listing.objects.filter(status=False) 
    
    return render(request, "auctions/index.html",{
        "listings": listings    
    })



def categories(request):
    return render(request, "auctions/categories.html",{
        "categories": Category.objects.all()
    })



def category(request, category_id):
    category = Category.objects.get(id=category_id)

    return render(request, "auctions/category.html",{
        "category": category,
        "listings": category.sort.all()
    })



def create_listing(request):  
    if request.method == "POST":
       form = ListingForm(request.POST, request.FILES)
       if form.is_valid():
           newlisting = form.save(commit=False)
           newlisting.user = request.user
           newlisting.save()
           return redirect('/')

    return render(request, "auctions/create_listing.html", {
        "form": ListingForm()
    })


@login_required(login_url='/login')
def listing(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    listing_status = Listing.objects.get(id=listing_id)
    listing_status = listing_status.status
    user = listing.user
    starting_price = listing.starting_price
    watch = Watchlist.objects.filter(user=request.user, listing=listing)
    bid = Bid.objects.filter(listing=listing)   
  
    if bid:
        price = Bid.objects.get(listing=listing)
        current_price = price.bid_price
        winner = price.user

    else:
        current_price = starting_price
        winner = 'not'

    if request.method == "POST":

        if 'watchlist' in request.POST:
            watchlist = Watchlist()
            watchlist.user = request.user
            watchlist.listing = listing
            
            if not request.user.watchlist.filter(listing=listing):
                 watchlist.save()

            else:
                request.user.watchlist.filter(listing=listing).delete()
            return HttpResponseRedirect(reverse('listing', args=(listing.id,)))

        elif 'bid' in request.POST: 

            form = BidForm(request.POST)
            posted_price = request.POST['bid_price']

            if float(posted_price) < starting_price or float(posted_price) < current_price:
                return render(request, "auctions/listing.html",{
                    "watch": watch,
                    "listing": listing,
                    "bid": bid,
                    "starting_price": starting_price,
                    "current_price": current_price,
                    "error": 'Price entered must be higher than the current bid.',
                    "form": CommentForm(),
                    "bid_form": BidForm(),
                    "comments": listing.item.all().order_by('time').reverse(),
                    "user_condition": user == request.user
                })
            
            elif not bid and float(posted_price) > starting_price:                
                if form.is_valid():
                    newbid = form.save(commit=False)
                    newbid.user = request.user
                    newbid.listing = listing
                    newbid.save()

            elif bid and float(posted_price) > current_price:
                
               bid.update(user=request.user, bid_price=posted_price)
            return HttpResponseRedirect(reverse('listing', args=(listing.id,)))
     
        elif 'close' in request.POST:
            listing_update = Listing.objects.filter(id=listing_id)
            listing_update = listing_update.update(status=True)
            
            return HttpResponseRedirect(reverse('listing', args=(listing.id,)))

        else:
            form = CommentForm(request.POST)
            if form.is_valid():
                newcomment = form.save(commit=False)
                newcomment.user = request.user
                newcomment.listing = listing
                newcomment.save()
                return HttpResponseRedirect(reverse('listing', args=(listing.id,)))

    return render(request, "auctions/listing.html",{
        "watch": watch,
        "listing": listing,
        "bid": bid,
        "starting_price": starting_price,
        "current_price": current_price,
        "form": CommentForm(),
        "bid_form": BidForm(),
        "comments": listing.item.all().order_by('time').reverse(),
        "user_condition": user == request.user,
        "win_condition": request.user == winner,
        "listing_status": listing_status == True
    })
        


def watchlist(request, uer_id):
    user = User.objects.get(id=uer_id)
    watch = Watchlist.objects.filter(user=user)
    return render(request, "auctions/watchlist.html",{
     "Watchlists": watch
    })
    


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")



@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))



def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

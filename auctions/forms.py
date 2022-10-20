from django import forms
from django.forms import ModelForm

from .models import * 


class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'category', 'description', 'starting_price', 'url']
        widgets = {
                   'title': forms.TextInput(attrs={'class': 'form-control'}),
                   'category' : forms.Select(choices=Category.objects.all(), attrs={'class' : 'form-control col-4'}),
                   'description' : forms.Textarea(attrs={'class': 'form-control'}),
                   'starting_price': forms.NumberInput(attrs={'class': 'form-control'}),
                   'url': forms.TextInput(attrs={'class': 'form-control'})
                   } 



class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        widgets = {
                   'comment': forms.Textarea(attrs={'cols': 70, 'rows': 5, 'placeholder': ' Add a comment'})
                   } 
        labels = {
                   'comment': ''
                  }



class BidForm(ModelForm):
    class Meta:
        model = Bid
        fields = ['bid_price']
        widgets = {
                   'bid_price': forms.NumberInput(attrs={'class': 'row',  'placeholder': ' Place your bid'})
                   } 
        labels = {
                   'bid_price': ''
                  }
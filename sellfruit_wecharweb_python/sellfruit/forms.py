__author__ = 'chenrenzhan'

from django import forms

class BuyFoorm(forms.Form):
    apple = forms.IntegerField(required=False)
    banana = forms.IntegerField(required=False)
    pear = forms.IntegerField(required=False)
    lemon = forms.IntegerField(required=False)

class OrderForm(forms.Form):
    delivery = forms.BaseForm()
    dorm = forms.CharField(max_length=4, required=False)
    phone = forms.CharField(max_length=11)


class CommentForm(forms.Form):
    comment = forms.CharField(max_length=forms.Textarea)



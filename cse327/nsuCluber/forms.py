from django import forms
from . import models
# This file is use for creating form of our website

class EventPostModelForm(forms.ModelForm):
    title = forms.CharField(label='Title')
    start = forms.CharField(label='Start')
    end = forms.CharField(label='End')
    place = forms.CharField(label='Place')
    owner = forms.ModelChoiceField(queryset=models.AllAdmins.objects.all(),label='Owner')
    eventSummary = forms.CharField(label='Event Summary')
    eventDetails = forms.CharField(label='Event Details',widget=forms.Textarea)
    keyWord = forms.CharField(label='Key Word')
    
    title.widget.attrs.update({"class":"form-control"})
    start.widget.attrs.update({"class":"form-control"})
    end.widget.attrs.update({"class":"form-control"})
    place.widget.attrs.update({"class":"form-control"})
    owner.widget.attrs.update({"class":"form-control"})
    eventSummary.widget.attrs.update({"class":"form-control"})
    eventDetails.widget.attrs.update({"class":"form-control"})
    keyWord.widget.attrs.update({"class":"form-control"})
    
    class Meta:
        model = models.EventPost
        fields = ['title','start','end','place','owner','eventSummary','eventDetails','keyWord']
from django import forms
from . import models
# This file is use for creating form of our website

class EventPostModelForm(forms.ModelForm):
    title = forms.CharField(max_length = 30)
    start = forms.DateTimeField(auto_now = False, auto_now_add = False)
    end = forms.DateTimeField(auto_now = False, auto_now_add = False)
    place = forms.CharField(max_length = 20)
    owner = forms.ForeignKey(models.AllAdmins,on_delete = models.CASCADE)
    eventSummary = forms.CharField(max_length = 100)
    eventDetails = forms.TextField()
    keyWord = forms.CharField(max_length = 50)
    
    title.widget.attrs.update({"class":"form-control-sm"})
    start.widget.attrs.update({"class":"form-control-sm"})
    end.widget.attrs.update({"class":"form-control-sm"})
    place.widget.attrs.update({"class":"form-control-sm"})
    owner.widget.attrs.update({"class":"form-control-sm"})
    eventSummary.widget.attrs.update({"class":"form-control-sm"})
    eventDetails.widget.attrs.update({"class":"form-control-sm"})
    keyWord.widget.attrs.update({"class":"form-control-sm"})
    class Meta:
        model = models.EventPost
        fields = ['title','start','end','place','owner','eventSummary','eventDetails','keyWord']
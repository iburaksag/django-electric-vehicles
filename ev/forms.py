from django import forms
from .models import EV, EVReview


class EVSearchForm(forms.Form):
    name = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class' : 'form-control' }))
    manufacturer = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class' : 'form-control' }))
    min_battery_size = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Min.' }))
    max_battery_size = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Max.' }))
    min_wltp_range = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Min.' }))
    max_wltp_range = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Max.' }))
    min_cost = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Min.' }))
    max_cost = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Max.' }))
    min_power = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Min.' }))
    max_power = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Max.' }))



class EVDetailForm(forms.ModelForm):
    class Meta:
        model = EV
        fields = ('name', 'manufacturer', 'battery_size', 'wltp_range', 'cost', 'power',)
    
    def __init__(self, *args, **kwargs):
        super(EVDetailForm, self).__init__(*args, **kwargs)

        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control'



class EVReviewForm(forms.ModelForm):
    class Meta:
        model = EVReview
        fields = ['review_text', 'rating']
        widgets = {
            'review_text': forms.Textarea(attrs={'class': 'form-control mb-3'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control mb-4'}),
        }        
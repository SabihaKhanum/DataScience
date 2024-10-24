from django import forms
from .models import CustomerFeedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = CustomerFeedback
        fields = ['review']
        widgets = {
            'review': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
        }
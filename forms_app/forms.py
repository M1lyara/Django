import re
from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['first_name', 'last_name', 'phone']

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        
        digits = re.sub(r'\D', '', phone)
        if len(digits) != 11:
            raise forms.ValidationError("Номер должен содержать 11 цифр")
        
        if Feedback.objects.filter(phone=phone).exists():
            raise forms.ValidationError("Этот номер уже оставил заявку!")
            
        return phone
from django import forms

from .models import User_details

# class UserForm(forms.Form):
#     name = forms.CharField(label="Your Name", label_suffix="", widget=forms.TextInput(attrs={'class': 'form-control'}))
#     email = forms.EmailField(required=False, label="Your Email", label_suffix="", help_text="We will never share your email with anyone else.", 
#                              widget=forms.EmailInput(attrs={'class': 'form-control'}))
#     Contact_number = forms.IntegerField(required=False, label="Contact Number", label_suffix="", widget=forms.NumberInput(attrs={'class': 'form-control'}))
#     bio= forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Bio'}))
 
#     def clean(self):
#         cleaned_data = super().clean()
#         # name = self.cleaned_data['name']
#         # mail = self.cleaned_data['email']

        
class UserForm(forms.ModelForm):
    class Meta:
        model =User_details
        fields='__all__'
        # exclude=['mail']
        labels={
            'name' : "Your Name",
            'mail' : "Your Mail",
            'contact_number' : "Your Contact Number",
            'bio' : "Your Details"
        }
        widgets={
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'mail': forms.EmailInput(attrs={'class': 'form-control'}),
            'contact_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
        }
    
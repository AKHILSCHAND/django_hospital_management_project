from django import forms
from .models import Booking, ContactMessage

class DateInput(forms.DateInput):
    input_type = 'date'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

        widgets = {
            'booking_date': DateInput(),
            
        }

        labels = {
           'p_name':'Patient Name',
           'p_phone':'Phone Number',
           'p_email':'Email',
           'dep_name':'Department Name',
           'doc_name':'Doctor Name',
           'booking_date':'Booking Date',
        }
       
class ContactForm(forms.ModelForm):

    class Meta:
        model = ContactMessage
        # fields = '__all__'
        fields = ['name', 'email', 'subject', 'message']
        
        widgets = {
            # 'contact_date': DateInput(),
            'message': forms.Textarea(attrs={'rows': 4, 'cols': 40, 'class':'border rounded w-full'})
            
        }
        # labels = {
        #    'name':'Name',
        #    'email':'Email',
        #    'subject':'Subject',
        #    'message':'message ',
        # }
        
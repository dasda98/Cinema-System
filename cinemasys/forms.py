from django.forms import ModelForm
from django.forms import DateInput
from .models import Seance, Reservations, Client, TypeOfTicket


class DateInput(DateInput):
    input_type = 'date'


class SeanceDateForm(ModelForm):
    class Meta:
        model = Seance
        fields = ['date']
        widgets = {
            "date": DateInput(),
        }


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'email', 'phone_number']

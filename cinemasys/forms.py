from django.forms import ModelForm, ValidationError, TextInput
from django.forms import DateInput
from .models import Seance, Reservations, Client, TypeOfTicket, Movie
from datetime import timedelta
from django.forms import ValidationError

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


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = "__all__"
        widgets = {
            "duration": TextInput(attrs={'placeholder': '<time> min'})
        }


class SeanceForm(ModelForm):
    class Meta:
        model = Seance
        fields = "__all__"
        widgets = {
            "hour": TextInput(attrs={'placeholder': 'HH:MM'})
        }

    def clean(self):
        data = self.cleaned_data
        check_variable = []
        for seance in Seance.objects.all():
            # Checking date, hall_id and start/end time between
            if data['date'] == seance.date and data['hall_idhall'] == seance.hall_idhall:
                if timedelta(hours=int(data['hour'].split(':')[0]), minutes=int(data['hour'].split(':')[1])).total_seconds()/60 <= \
                    timedelta(hours=int(seance.hour.split(':')[0]), minutes=int(seance.hour.split(':')[1])).total_seconds()/60 <= \
                    timedelta(hours=int(data['hour'].split(':')[0]), minutes=int(data['hour'].split(':')[1])).total_seconds()/60 + timedelta(minutes=int(data['movie_idmovie'].duration.split(' ')[0])).total_seconds()/60 or \
                    timedelta(hours=int(data['hour'].split(':')[0]), minutes=int(data['hour'].split(':')[1])).total_seconds()/60 <= \
                    timedelta(hours=int(seance.hour.split(':')[0]), minutes=int(seance.hour.split(':')[1])).total_seconds()/60 + timedelta(minutes=int(seance.movie_idmovie.duration.split(' ')[0])).total_seconds()/60 <= \
                    timedelta(hours=int(data['hour'].split(':')[0]), minutes=int(data['hour'].split(':')[1])).total_seconds()/60 + timedelta(minutes=int(data['movie_idmovie'].duration.split(' ')[0])).total_seconds()/60:
                        check_variable.append(False)
                else:
                    check_variable.append(True)
            else:
                check_variable.append(True)
        if False not in check_variable:
            return data
        else:
            raise ValidationError("The session cannot be at the same date, time and in the same room as another.")

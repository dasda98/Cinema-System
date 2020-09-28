from django.db import models
from datetime import timedelta
from django.forms import ValidationError
from django.contrib import admin

"""
class Login(models.Model):
    password = models.CharField(max_length=45)
    login = models.CharField(max_length=45)

class Admin(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    job_position = models.CharField(max_length=45)
    login_idlogin = models.ForeignKey(Login, on_delete=models.CASCADE)
"""


class Client(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(max_length=100)
    phone_number = models.IntegerField()


class Hall(models.Model):
    hall_name = models.CharField(max_length=45)
    seats = models.IntegerField()


class Movie(models.Model):
    title = models.CharField(max_length=45)
    director = models.CharField(max_length=45)
    year_of_production = models.IntegerField()
    duration = models.CharField(max_length=10)
    country = models.CharField(max_length=45)
    cast = models.TextField()
    age_limit = models.CharField(max_length=3)
    type = models.CharField(max_length=45)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', default=1)


class Seance(models.Model):
    date = models.DateField()
    hour = models.CharField(max_length=5)
    movie_idmovie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    hall_idhall = models.ForeignKey(Hall, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        check_variable = []
        for seance in Seance.objects.all():
            # Checking date, hall_id and start/end time between
            if self.date == seance.date and \
            timedelta(hours=int(self.hour.split(':')[0]), minutes=int(self.hour.split(':')[1])).total_seconds()/60 <= \
            timedelta(hours=int(seance.hour.split(':')[0]), minutes=int(seance.hour.split(':')[1])).total_seconds()/60 <= \
            timedelta(hours=int(self.hour.split(':')[0]), minutes=int(self.hour.split(':')[1])).total_seconds()/60 + timedelta(minutes=int(self.movie_idmovie.duration.split(' ')[0])).total_seconds()/60 or \
            timedelta(hours=int(self.hour.split(':')[0]), minutes=int(self.hour.split(':')[1])).total_seconds()/60 <= \
            timedelta(hours=int(seance.hour.split(':')[0]), minutes=int(seance.hour.split(':')[1])).total_seconds()/60 + timedelta(minutes=int(seance.movie_idmovie.duration.split(' ')[0])).total_seconds()/60 <= \
            timedelta(hours=int(self.hour.split(':')[0]), minutes=int(self.hour.split(':')[1])).total_seconds()/60 + timedelta(minutes=int(self.movie_idmovie.duration.split(' ')[0])).total_seconds()/60 and \
            self.hall_idhall == seance.hall_idhall:
                check_variable.append(False)
            else:
                check_variable.append(True)
        if False not in check_variable:
            super(Seance, self).save(*args, **kwargs)
        else:
            raise ValidationError("The session cannot be at the same date, time and in the same room as another.")


class Reservations(models.Model):
    seance_idseance = models.ForeignKey(Seance, on_delete=models.CASCADE)
    client_idclient = models.ForeignKey(Client, on_delete=models.CASCADE)


class TypeOfTicket(models.Model):
    type = models.CharField(max_length=45)
    price = models.IntegerField()


class Ticket(models.Model):
    row = models.CharField(max_length=2, default=0)
    col = models.CharField(max_length=2, default=0)
    type_of_ticket_idtypeofticket = models.ForeignKey(TypeOfTicket, on_delete=models.CASCADE, default=0)
    seance_idseance = models.ForeignKey(Seance, on_delete=models.CASCADE, default=0)

from django.db import models
from datetime import timedelta
from django.forms import ValidationError


class Client(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(max_length=100)
    phone_number = models.IntegerField()

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Hall(models.Model):
    hall_name = models.CharField(max_length=45)
    seats = models.IntegerField()

    def __str__(self):
        return "{}".format(self.hall_name)


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

    def __str__(self):
        return "{}".format(self.title)


class Seance(models.Model):
    date = models.DateField()
    hour = models.CharField(max_length=5)
    movie_idmovie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    hall_idhall = models.ForeignKey(Hall, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.movie_idmovie.title)


class Reservations(models.Model):
    seance_idseance = models.ForeignKey(Seance, on_delete=models.CASCADE)
    client_idclient = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.seance_idseance.date, self.client_idclient)


class TypeOfTicket(models.Model):
    type = models.CharField(max_length=45)
    price = models.IntegerField()

    def __str__(self):
        return "{}".format(self.type)


class Ticket(models.Model):
    row = models.CharField(max_length=2, default=0)
    col = models.CharField(max_length=2, default=0)
    type_of_ticket_idtypeofticket = models.ForeignKey(TypeOfTicket, on_delete=models.CASCADE, default=0)
    seance_idseance = models.ForeignKey(Seance, on_delete=models.CASCADE, default=0)

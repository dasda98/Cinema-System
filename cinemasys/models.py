from django.db import models
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

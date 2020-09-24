from django.contrib import admin
from .models import Movie, Hall, Seance, TypeOfTicket, Client, Reservations, Ticket


admin.site.register(Movie)
admin.site.register(Hall)
admin.site.register(Seance)
admin.site.register(TypeOfTicket)
admin.site.register(Client)
admin.site.register(Reservations)
admin.site.register(Ticket)

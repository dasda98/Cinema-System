from django.contrib import admin
from .models import Movie, Hall, Seance, TypeOfTicket, Client, Reservations, Ticket
from .forms import SeanceForm, MovieForm


class SeanceAdmin(admin.ModelAdmin):
    form = SeanceForm

    list_display = ("movie_idmovie", "date", "hour", "hall_idhall")
    list_filter = ("date",)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["movie_idmovie"].label = "Movie"
        form.base_fields["hall_idhall"].label = "Hall"
        return form


class ClientAdmin(admin.ModelAdmin):
    search_fields = ("last_name__startswith",)


class ReservationsAdmin(admin.ModelAdmin):
    list_display = ("client_idclient",
                    "seance_idseance",
                    "seance_date",)
    list_filter = ("seance_idseance__date",)
    search_fields = ("client_idclient__last_name",)

    def seance_date(self, obj):
        return obj.seance_idseance.date


class MovieAdmin(admin.ModelAdmin):
    form = MovieForm


admin.site.register(Movie, MovieAdmin)
admin.site.register(Hall)
admin.site.register(Seance, SeanceAdmin)
admin.site.register(TypeOfTicket)
admin.site.register(Client, ClientAdmin)
admin.site.register(Reservations, ReservationsAdmin)
admin.site.register(Ticket)

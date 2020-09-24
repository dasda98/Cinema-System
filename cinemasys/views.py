from django.views import generic
from django_filters.views import FilterView
from django.shortcuts import render, HttpResponse
from .models import Movie, Seance, TypeOfTicket, Reservations, Ticket
from .filters import SeanceDateFilter
from .forms import SeanceDateForm, ClientForm
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import datetime


class IndexView(generic.ListView):
    template_name = 'cinemasys/index.html'
    context_object_name = 'lastest_movie_list'

    def check_seance_date(self):
        for senace in Seance.objects.all():
            if senace.date <= datetime.date.today() and \
                    senace.hour <= str(datetime.datetime.now().hour) + ':' +\
                    str(datetime.datetime.now().minute):
                senace.delete()

    def get_queryset(self):
        self.check_seance_date()
        return Movie.objects.order_by('-year_of_production')[:5]


class DetailView(generic.DetailView):
    model = Movie
    template_name = 'cinemasys/detail.html'


class SeanceView(generic.CreateView, FilterView):
    template_name = 'cinemasys/seance_list.html'
    filterset_class = SeanceDateFilter
    form_class = SeanceDateForm


def BuyTicketView(request, seance_id):
    template_name = 'cinemasys/buy_ticket_test.html'
    seance = Seance.objects.get(pk=seance_id)
    type_of_ticket = TypeOfTicket.objects.all()
    ticket_seats = Ticket.objects.filter(seance_idseance=seance_id)
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save()
            reservation = Reservations(seance_idseance=seance,
                                       client_idclient=client)
            reservation.save()
            type_of_ticket_POST = TypeOfTicket.objects.get(pk=request.POST['controlS'])
            ticket = Ticket(row=request.POST['checkBoxSeat'][0],
                            col=request.POST['checkBoxSeat'][1],
                            type_of_ticket_idtypeofticket=type_of_ticket_POST,
                            seance_idseance=seance)
            ticket.save()
            subject = 'Your booking has been made successfully'
            html_message = render_to_string('cinemasys/send_email.html')
            content = html_message.format(client.first_name, client.last_name,
                       seance.movie_idmovie.title,
                       seance.date,
                       seance.hour,
                       seance.hall_idhall.hall_name,
                       ticket.row, ticket.col)
            plain_message = strip_tags(content)
            send_mail(subject, plain_message, "test.django98@gmail.com", [client.email], html_message=content)
            return render(request, 'cinemasys/buy_ticket_success.html')
    else:
        form_class = ClientForm

        return render(request, template_name,
                      {'form': form_class,
                       'seance': seance,
                       'type_of_ticket': type_of_ticket,
                       'ticket_seats': ticket_seats,
                       })


class PricingView(generic.ListView):
    template_name = 'cinemasys/pricing.html'
    context_object_name = 'type_list'

    def get_queryset(self):
        return TypeOfTicket.objects.all()

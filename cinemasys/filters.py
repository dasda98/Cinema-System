from .models import Seance
import django_filters


class SeanceDateFilter(django_filters.FilterSet):
    class Meta:
        model = Seance
        fields = ['date']

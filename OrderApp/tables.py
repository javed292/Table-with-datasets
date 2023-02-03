import django_tables2 as tables
from .models import Table


class OrderTable(tables.Table):

    class Meta:
        attrs = {"class": "table table-stripped","data-add-url":"Url here"}
        model = Table
        # fields = "__all__"

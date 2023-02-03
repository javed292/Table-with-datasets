from django.shortcuts import render,redirect
from .models import Table
from .tables import OrderTable
from .forms import TableForm
from django.views.decorators.csrf import requires_csrf_token
# Create your views here.
def index(request):
    items = Table.objects.all()
    sort = request.GET.get('sort',None)
    if sort:
        items = items.order_by(sort)
    table = OrderTable(items)
    context = {
        "Objects" : items,
        "table" : table
    }
    return render(request,'table.html',context)

@requires_csrf_token
def add_order(request):
    if request.method == "POST":
        form = TableForm(request.POST)
        if form.is_valid():
            item = form.save()
            return redirect('home')
    else:
        form = TableForm()
    context = {
        'form': form
    }
    return render(request,"addOrder.html",context)
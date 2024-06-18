from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import MyData, Signals
from django.views.decorators.csrf import csrf_exempt

def add_data(request):
    if request.method == 'POST':
        name = request.POST['name']
        value = request.POST['value']
        MyData.objects.create(name=name, value=value)
        return redirect('show_data')
    return HttpResponse("Only POST requests are allowed.")

def show_data(request):
    data = MyData.objects.all()
    return render(request, 'myapp/show_data.html', {'data': data})

@csrf_exempt
def post_signal(request):
    if request.method == 'POST':
        stock_name = request.POST['stock_name']
        strategy_name = request.POST['strategy_name']
        signal = request.POST['signal']
        date_time = request.POST['date_time']
        price = request.POST['price']
        final_portfolio_value = request.POST['final_portfolio_value']
        Signals.objects.create(stock_name=stock_name, strategy_name=strategy_name, signal=signal, date=date, time=time, price=price, final_portfolio_value=final_portfolio_value)
        return redirect('show_signals')
    return HttpResponse("Only POST requests are allowed.")

def show_signals(request):
    signals = Signals.objects.all()
    return render(request, 'myapp/show_signals.html', {'signals': signals})
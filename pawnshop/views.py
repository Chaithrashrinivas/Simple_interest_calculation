from django.shortcuts import render
from .models import User

# Create your views here.
def interest_calculation(request):
    if request.method == "GET":
        return render(request)
    elif request.method == "POST":
        start_date = request.POST.get('start date')
        end_date = request.POST.get('end date')
        principal = request.POST.get('principal')
        interest = request.POST.get('interest')
    p = principal_amount, i = interest_rate, si = simple_interest, r = rate, d = day, t = total_amount
    for interest in calculate:
        if principal_amount<5000:
            interest_rate = 3/100
        else principal_amount>5001:
            interest_rate = 2/100
    simple_interest = ((p * r * d) / 100)
    interest_rate per month = number of 100s in principal_amount * interest_rate = (5000 / 100) * 3 = rs.150
    interest_rate for months = interest_rate per month * no.of months = total_amount
    interest_rate for days = (interest_rate per month / 30) * no.of days = total_amount











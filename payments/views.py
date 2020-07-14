from django.shortcuts import render, redirect
from .models import Payment
from .forms import PaymentForm
from .resources import PaymentResource

# from .resources import PaymentResource
from django.contrib import messages
from tablib import Dataset, core
from django.http import HttpResponse

# function to list payments
def list_payments(request):
    payments = Payment.objects.all()
    return render(request ,'payments.html',{'payments': payments}) 

# function to create a new payment
def create_payment(request):
    form = PaymentForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_payments')
    
    return render(request, 'payments-form.html', {'form':form})

# function to update an record
def update_payment(request, id):
    payment = Payment.objects.get(id=id)
    form = PaymentForm(request.POST or None, instance=payment)
    
    if form.is_valid():
        form.save()
        return redirect('list_payments')
    
    return render(request, 'payments-form.html', {'form':form, 'payment':payment})

# function to delete a selected payment
def delete_payment(request, id):
    payment = Payment.objects.get(id=id)

    if request.method == 'POST':
        payment.delete()
        return redirect('list_payments')
    
    return render(request, 'payment-delete-confirm.html', {'payment':payment})

#function to upload a xlsx file and save the informations on the database
def upload(request):
    if request.method == 'POST':
        payment_resource = PaymentResource()
        dataset = Dataset()
        new_payment = request.FILES['myfile']

        if not new_payment.name.endswith('xlsx'):
            messages.info(request,'Wrong Format')
            return render(request, 'upload.html')

        imported_data = dataset.load(new_payment.read(),format='xls')
      
        for data in imported_data:
                value = Payment(
                    data[0], #id
                    data[1], #title
                    data[3], #value
                    data[2], #date
                    0, #tax
                    data[4], #comment
                )
                value.save()
    return render(request, 'upload.html')

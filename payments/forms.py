from django import forms
from .models import Payment

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'
        exclude = ('externalTax',)
        

    def __init__(self, *args, **kwargs):
        super(PaymentForm,self).__init__(*args,**kwargs)
        self.fields['comment'].required = False


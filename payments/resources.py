from import_export import resources
from .models import Payment

class PaymentResource(resources.ModelResource):
    class meta:
        model = Payment
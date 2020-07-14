from django.db import models
from django.core.validators import MinLengthValidator

#class payment saves informations of each payment
class Payment(models.Model):
    title = models.CharField(max_length=100,validators=[MinLengthValidator(5)])
    value = models.FloatField()
    date = models.DateField()
    externalTax = models.FloatField()
    comment = models.TextField()
    
    #calculates the external tax
    @property
    def get_externalTax(self):
        return 0.05*self.value

    def __str__(self):
        return self.title

    #save the external tax calculated
    def save(self, *args, **kwargs):
          self.externalTax = self.get_externalTax
          super(Payment, self).save(*args, **kwargs)
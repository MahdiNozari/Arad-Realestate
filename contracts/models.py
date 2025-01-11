from django.db import models
from accounts.models import  Customer,Agent
from home.models import File
from django.conf import settings
class Contract(models.Model):
    title=models.CharField(max_length=50)
    image=models.ImageField(default='')
    serial=models.BigIntegerField(unique=True, primary_key=True)
    seller_customer=models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='seller_contracts')
    buyer_customer=models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='buyer_contracts')
    agent=models.ForeignKey(Agent,on_delete=models.CASCADE,related_name='agent_contracts')
    file=models.ForeignKey(File,on_delete=models.CASCADE)
    percent=models.BigIntegerField()
    price=models.BigIntegerField(default=0)
    date=models.DateField()
    credit=models.DateField()
    
    def __str__(self):
        return f"قرارداد ملک {self.file.title} بین {self.seller_customer} و {self.buyer_customer}"
    
    class Meta:
        verbose_name = "قرارداد"
        verbose_name_plural = "قراردادها"
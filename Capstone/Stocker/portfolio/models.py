from django.db import models
from django.conf import settings

"""
The following code is thanks to Joe and his amazing troubleshooting abilities.
"""

class Company(models.Model):
    # one stock model per company - 1x Apple, 1x Tesla, etc...
    
    name = models.CharField(max_length=100)
    ticker_symbol = models.CharField(max_length=5)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    
    def __str__(self):
        return f"{self.name} - {self.ticker_symbol}"

# look into this if we get to doing it on time
# it's easy yeet yeet
class Holdings(models.Model):
    # one element per stock per user
    # This class would simply represent an amount of a single stock
    # that is owned by a single person.
    # so if I own 3x Tesla, then I create one Holdings entry for
    # Tesla that has a count of 3... then that Holdings entry is
    # added to my personal portfolio and updated from the portfolio
    # side. Once we create this element, we never reference it through
    # the Holdings class again.
    
    stock = models.ForeignKey(Company, on_delete=models.DO_NOTHING)
    count = models.IntegerField()
    
    def __str__(self):
        return f"{self.stock.name} - {self.count}"


class Portfolio(models.Model):
    # This relationship is all of the holdings of a particular user.
    # There is one Holdings entry for each different stock, and the
    # Holdings entry tells us how many of each stock we own. Example
    #
    # usage:
    # request.user.portfolio.stocks.filter(stock__ticker_symbol='TSLA')
    
    name = models.CharField(max_length=40)
    stocks = models.ManyToManyField(Holdings, blank=True)
    owner = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.owner.username}'s portfolio"



"""
myport = request.user.portfolio
stock = Stock.objects.filter(ticker_symbol=THING)
if myport.stocks.filter(stock=stock):
  mystock = myport.stocks.get(stock=stock)
  mystock.count += 1
  mystock.save()
"""
from django.contrib import admin

from .models import BasicDetail, LoanAccount, Customer

admin.site.register(BasicDetail)
admin.site.register(LoanAccount)
admin.site.register(Customer)

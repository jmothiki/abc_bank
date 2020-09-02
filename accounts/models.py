import uuid

from django.db import models
from django.urls import reverse


class BasicDetail(models.Model):
    """Model representing basic details of customer"""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    aadhar = models.IntegerField(unique=True)
    pan = models.CharField(max_length=10, unique=True, null=True, blank=True)
    Phone = models.IntegerField(unique=True)
    email = models.EmailField(null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the url to access the particular customer details"""
        return reverse('customer detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object"""
        return f'{self.last_name} {self.first_name}'


class LoanAccount(models.Model):
    """Model representing loan details of customer"""
    loan_no = models.UUIDField(primary_key=True, default=uuid.uuid4)
    l_type = [
        ('PRS', 'Personal Loan'),
        ('HOU', 'Housing Loan'),
        ('MRT', 'Mortgage Loan'),
        ('GLD', 'Gold Loan')
    ]
    loan_type = models.CharField(max_length=3, choices=l_type)
    loan_amount_issued = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        ordering = ['loan_no']

    def get_absolute_url(self):
        return reverse('loan account num', args=[str(self.id)])

    def __str__(self):
        return f'{self.loan_no}, {self.loan_type}'


class Customer(models.Model):
    customer_id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this customer "
                                                                                   "across the whole bank.")
    account_no = models.IntegerField(unique=True)
    details = models.ForeignKey(BasicDetail, on_delete=models.RESTRICT)
    a_type = [
        ('SB', 'Savings Account'),
        ('CB', 'Current Account'),
    ]
    acc_type = models.CharField(max_length=2, choices=a_type)
    loan = models.ForeignKey(LoanAccount, on_delete=models.RESTRICT)

    def __str__(self):
        return f'{self.account_no}'

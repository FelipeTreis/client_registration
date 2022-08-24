from django.db import models

from register.choices import STATE_CHOICES


class Customer(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    surname = models.CharField(max_length=65, null=False, blank=False)
    birth_date = models.DateField(auto_now_add=False, null=False, blank=False)
    rg = models.CharField(max_length=7, null=False, blank=False)
    cpf = models.CharField(max_length=11, null=False, blank=False)
    cnpj = models.CharField(max_length=14, null=True, blank=True)
    mother_name = models.CharField(max_length=95, null=True, blank=True)
    phone = models.CharField(max_length=15, null=False, blank=False)
    country = models.CharField(
        max_length=25, null=False, blank=False,
        default='Brazil'
    )
    state = models.CharField(
        max_length=2, null=False,
        blank=False, choices=STATE_CHOICES, default=''
    )
    city = models.CharField(max_length=30, null=False, blank=False)
    neighborhood = models.CharField(max_length=30, null=False, blank=False)
    street = models.CharField(max_length=30, null=False, blank=False)
    number = models.IntegerField(null=False, blank=False)
    note = models.TextField(null=True, blank=True)

    @property
    def full_name(self):
        return f'{self.name} {self.surname}'

    @property
    def address(self):
        return f'{self.city}: {self.street}-{self.number}, {self.neighborhood}'

    def __str__(self):
        return self.full_name

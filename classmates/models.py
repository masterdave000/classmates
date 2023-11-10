from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class Classmate(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    age = models.IntegerField()
    address = models.CharField(max_length=200, default='No Address Added')
    gender = models.CharField(max_length=200, default='No Gender Provided')

    def clean(self):
        super().clean()

        if any(c.isdigit() for c in self.firstname):
            raise ValidationError({'firstname': _("First name cannot contain numbers.")})

        if any(c.isdigit() for c in self.lastname):
            raise ValidationError({'lastname': _("Last name cannot contain numbers.")})

        if len(self.address) < 5:
            raise ValidationError({'address': _("Address should be at least 5 characters long.")})

        # Example gender validation - you can define more specific rules here
        valid_genders = ['Male', 'Female', 'Other', 'male', 'female', 'other']
        if self.gender not in valid_genders:
            raise ValidationError({'gender': _("Invalid gender provided. Please select between 'Male', 'Female', 'Other', 'male', 'female', 'other'")})

        if self.age <= 0:
            raise ValidationError({'age': _("Age cannot be negative or zero.")})

    def __str__(self):
        return self.firstname

    def get_absolute_url(self):
        return reverse('classmate_edit', kwargs={'pk': self.pk})

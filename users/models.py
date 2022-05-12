from django.db import models
from django.contrib.auth.models import User


class CustomUser(User):
    GENDER_TYPE = (
        ("MALE", "Male"),
        ("FEMALE", "Female"),
        ("OTHER", "Other")
    )
    OCCUPATION_CHOICE = (
        ("STUDENT", "STUDENT"),
        ("WORKER", "WORKER"),
        ("JOBLESS", "JOBLESS"),
        ("RETIRED", "RETIRED"),
    )
    gender = models.CharField(choices=GENDER_TYPE, max_length=100)
    occupation = models.CharField(choices=OCCUPATION_CHOICE, max_length=100)
    phone_number = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

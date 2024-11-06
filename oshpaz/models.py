from django.db import models

class Profession(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Certificate(models.Model):
    file = models.FileField(upload_to='certificates/')  

    def __str__(self):
        return f"Certificate {self.id}"


class Achievement(models.Model):
    image = models.ImageField(upload_to='achievements/')  

    def __str__(self):
        return f"Achievement {self.id}"


class User(models.Model):
    MALE = 1
    FEMALE = 2
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]

    GOOGLE = 1
    FACEBOOK = 2
    AUTH_TYPE_CHOICES = [
        (GOOGLE, 'Google'),
        (FACEBOOK, 'Facebook'),
    ]

    full_name = models.CharField(max_length=255)
    phone = models.BigIntegerField(null=True, blank=True)
    gender = models.IntegerField(choices=GENDER_CHOICES)
    birth_of_date = models.DateField()
    email = models.EmailField(unique=True, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    profession = models.ForeignKey(Profession, on_delete=models.SET_NULL, null=True, blank=True)
    certificate = models.ForeignKey(Certificate, on_delete=models.SET_NULL, null=True, blank=True)
    achievement = models.ForeignKey(Achievement, on_delete=models.SET_NULL, null=True, blank=True)
    work_place = models.CharField(max_length=255, null=True, blank=True)
    auth_type = models.IntegerField(choices=AUTH_TYPE_CHOICES)
    is_blocked = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name
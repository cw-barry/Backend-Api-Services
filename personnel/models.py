from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name}"

class Personnel(models.Model):
    department = models.ForeignKey(Department, on_delete=models.PROTECT, related_name="staff")
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(null=True, blank=True)
    title = models.CharField(max_length=30)
    image = models.URLField(null=True, blank=True, default="https://source.unsplash.com/random/900x700/?person")
    GENDER = (
        ("1", "Male"),
        ("2", "Female"),
        ("3", "Prefer Not To Say"),
    )

    gender = models.CharField(max_length=1, choices=GENDER)

    date_joined = models.DateField()

    def __str__(self):
        return f"{self.department} {self.first_name} {self.last_name}"
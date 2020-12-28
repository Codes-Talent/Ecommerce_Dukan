from django.db import models

class Categary(models.Model):
    name = models.CharField(max_length=20)

    @staticmethod
    def get_all_categaries():
        return Categary.objects.all()

    def __str__(self):
        return self.name
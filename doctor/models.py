from django.db import models

# Create your models here.

specialities_choices = [
    ('Allgemeinmedizin', 'Allgemeinmedizin'),
    ('Radiologe', "Radiologe"),
    ('Hautarzt', 'Hautarzt')
]

title_choices = [
    ('Dr.', 'Dr.'),
    ('Prof. Dr.', 'Prof. Dr.'),
    ('Dr. rer. nat.', 'Dr. rer. nat.')
]


class Doctor(models.Model):
    name = models.CharField(max_length=30)
    speciality = models.CharField(max_length=30, choices=specialities_choices)
    title = models.CharField(max_length=30, choices=title_choices)

    def __str__(self):
        return self.title + self.name + ', Speciality: ' + self.speciality

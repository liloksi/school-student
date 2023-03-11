from django.db import models

from online_queue.models import Student
from school.models import School


class AchievementType(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Тип достижений'
        verbose_name_plural = 'Типы достижений'

    def __str__(self):
        return f'{self.name}'


class Profile(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class Achievement(models.Model):
    type = models.ForeignKey(AchievementType, on_delete=models.SET_NULL)
    name = models.CharField(max_length=100)
    date = models.DateField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Достижение'
        verbose_name_plural = 'Достижения'


class HistoryOfStudy(models.Model):
    date = models.DateField()
    school = models.ForeignKey(School, on_delete=models.SET_NULL)
    profile = models.ForeignKey(AchievementType, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'История обучения'




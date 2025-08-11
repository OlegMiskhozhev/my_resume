
from django.db import models

from my_resume import constants


class Institute(models.Model):
    name = models.CharField(
        'Название',
        max_length=constants.CHAR_LENGTH
    )
    logo = models.ImageField(
        'Логотип',
        upload_to='logos'
    )
    address = models.CharField(
        'Адрес',
        max_length=constants.CHAR_LENGTH
    )

    class Meta:
        verbose_name = 'Образовательное учреждение'
        verbose_name_plural = 'Образовательные учреждения'

    def __str__(self):
        return self.name


class Organisation(models.Model):
    name = models.CharField(
        'Название',
        max_length=constants.CHAR_LENGTH
    )
    logo = models.ImageField(
        'Логотип',
        upload_to='logos'
    )
    address = models.CharField(
        'Адрес',
        max_length=constants.CHAR_LENGTH
    )
    business_area = models.CharField(
        'Направление деятельности',
        max_length=constants.CHAR_LENGTH
    )

    class Meta:
        verbose_name = 'организация'
        verbose_name_plural = 'Организации'

    def __str__(self):
        return self.name


class Course(models.Model):

    institute = models.ForeignKey(
        Institute,
        on_delete=models.CASCADE,
        verbose_name='Образовательное учреждение',
        related_name='institutes'
    )
    program = models.CharField(
        'Образовательная программа',
        max_length=constants.CHAR_LENGTH
    )
    qualification = models.CharField(
        'Квалификация',
        max_length=constants.CHAR_LENGTH
    )

    class Meta:
        verbose_name = 'образовательная программа'
        verbose_name_plural = 'Образовательные программы'

    def __str__(self):
        return self.program


class WorkPlace(models.Model):
    organization = models.ForeignKey(
        Organisation,
        on_delete=models.CASCADE,
        verbose_name='Организация',
        related_name='organisations'
    )
    start_job = models.DateField(
        'Начало работы'
    )
    end_job = models.DateField(
        'Окончание работы'
    )
    position = models.CharField(
        'Должность',
        max_length=constants.CHAR_LENGTH
    )

    class Meta:
        verbose_name = 'место работы'
        verbose_name_plural = 'Места работы'
        ordering = ('-end_job',)

    def __str__(self):
        return self.organization.name


class Skill(models.Model):
    tool = models.CharField(
        'Инструмент',
        max_length=constants.CHAR_LENGTH
    )

    class Meta:
        verbose_name = 'инструмент'
        verbose_name_plural = 'Инструмент'

    def __str__(self):
        return self.tool


class Project(models.Model):
    name = models.CharField(
        'Название проекта',
        max_length=constants.CHAR_LENGTH
    )
    url = models.URLField(
        'Адрес проекта',
        max_length=constants.CHAR_LENGTH
    )
    release_date = models.DateField(
        'Дата релиза'
    )
    screenshot = models.ImageField(
        'Скриншот',
        upload_to='screenshots'
    )

    class Meta:
        verbose_name = 'проект'
        verbose_name_plural = 'Проекты'
        ordering = ('-release_date',)

    def __str__(self):
        return self.name

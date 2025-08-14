from datetime import date

from django.contrib.auth.models import AbstractUser
from django.db import models

from my_resume import constants
from resume.models import Course, Project, Skill, WorkPlace


class CustomUser(AbstractUser):
    """Модель для пользователей."""
    photo = models.ImageField(
        'Фото',
        upload_to='users_photo',
        blank=True,
        null=True
    )
    position = models.CharField(
        'Должность',
        max_length=constants.CHAR_LENGTH,
        blank=True,
        null=True
    )
    description = models.TextField(
        'Описание',
        blank=True,
        null=True
    )
    birthday = models.DateField(
        'Дата рождения',
        blank=True,
        null=True
    )
    location = models.CharField(
        'Место проживания',
        max_length=constants.CHAR_LENGTH,
        blank=True,
        null=True
    )
    phone_number = models.CharField(
        'Номер телефона',
        max_length=constants.CHAR_LENGTH,
        blank=True,
        null=True
    )
    github_profile = models.CharField(
        'GitHub профиль',
        max_length=constants.CHAR_LENGTH,
        blank=True,
        null=True
    )
    education = models.ManyToManyField(
        Course,
        through='UserEducation',
        verbose_name='Образование',
        blank=True,
    )
    skill = models.ManyToManyField(
        Skill,
        through='UserSkills',
        verbose_name='Навыки',
        blank=True,
    )
    work_place = models.ManyToManyField(
        WorkPlace,
        verbose_name='Места работы',
        blank=True,
    )
    project = models.ManyToManyField(
        Project,
        through='UserProjects',
        verbose_name='Проект пользователя',
        blank=True
    )

    @property
    def age(self):
        user_age = date.today() - self.birthday
        return user_age.days // 365


class UserEducation(models.Model):
    """Модель для образований пользователей с указанием периода прохождения."""
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    education = models.ForeignKey(Course, on_delete=models.CASCADE)
    start_program = models.DateField(
        'Начало обучения'
    )
    end_program = models.DateField(
        'Окончание обучения'
    )

    class Meta:
        verbose_name = 'образование пользователя'
        verbose_name_plural = 'Образования пользователей'
        default_related_name = 'user_educations'
        ordering = ('-end_program',)

    def __str__(self):
        return self.education.program


class UserSkills(models.Model):
    """Моедль для навыков пользователя с указанием уровня освоения."""
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    grade = models.CharField(
        'Уровень освоения',
        max_length=constants.CHAR_LENGTH,
        help_text='В процентах от 0 до 100'
    )

    class Meta:
        verbose_name = 'навык пользователя'
        verbose_name_plural = 'Навыки пользователей'
        default_related_name = 'user_skills'
        ordering = ('id',)

    def __str__(self):
        return self.skill.tool


class UserProjects(models.Model):
    """Модель для реализованных проектов пользователя
    с указанием уровня вовлеченности."""
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    involvement = models.CharField(max_length=constants.CHAR_LENGTH)

    class Meta:
        verbose_name = 'проект пользователя'
        verbose_name_plural = 'Проекты пользователя'
        default_related_name = 'user_projects'
        ordering = ('-id',)

    def __str__(self):
        return self.project.name

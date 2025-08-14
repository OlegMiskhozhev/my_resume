from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model

from resume.models import (
    Course, Institute, Project, Skill, Organisation, WorkPlace)
from users.models import UserEducation, UserProjects, UserSkills

User = get_user_model()


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    model = User
    fieldsets = BaseUserAdmin.fieldsets + (
        (None, {"fields": [
            'photo',
            'position',
            'description',
            'birthday',
            'location',
            'phone_number',
            'github_profile',
            'work_place',
        ]}),)
    list_display = (
        'id',
        'username',
        'email',
        'first_name',
        'last_name',
    )
    list_display_links = ('username',)
    filter_horizontal = ('work_place',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        'institute',
        'program',
        'qualification',
    )


@admin.register(UserEducation)
class UserEducationAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'education',
        'start_program',
        'end_program'
    )


@admin.register(Institute)
class InstituteAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'logo',
        'address'
    )


@admin.register(Organisation)
class OrganisationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'logo',
        'address'
    )


@admin.register(WorkPlace)
class WorkPlaceAdmin(admin.ModelAdmin):
    list_display = (
        'organization',
        'start_job',
        'end_job',
        'position'
    )


@admin.register(Skill)
class HardSkillAdmin(admin.ModelAdmin):
    list_display = (
        'tool',
    )


@admin.register(UserSkills)
class UserSkillAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'skill',
        'grade',
    )


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'url',
        'release_date',
        'screenshot',
    )


@admin.register(UserProjects)
class UserProjectsAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'project',
        'involvement',
    )

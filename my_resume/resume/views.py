from django.contrib.auth import get_user_model
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

from my_resume import constants

User = get_user_model()


class NewVersion(TemplateView):
    """Представление для вывода главной страницы проекта."""
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = get_object_or_404(User, username='miskhozhev')
        context = {
            'user': user,
            'user_educations': user.user_educations.all(),
            'user_skills': user.user_skills.all(),
            'user_projects': user.user_projects.all().order_by(
                '-project__release_date'),
            'sections': constants.SECTIONS
        }
        return context


def download(request, *args, **kwargs):
    """Позволяет скачать PDF файл с резюме пользователя."""
    response = FileResponse(
        open('media/resume.pdf', 'rb'),
        as_attachment=True,
        filename='resume.pdf'
    )
    return response

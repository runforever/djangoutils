# coding: utf-8

from django.views.generic import TemplateView

from .mixin_utils import (
    LoginRequiredMixin,
)


class LoginRequiredTplView(LoginRequiredMixin, TemplateView):
    pass

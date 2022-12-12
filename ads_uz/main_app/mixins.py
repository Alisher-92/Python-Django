from django.contrib import messages
from django.shortcuts import redirect
from django.views import View


class IsAuthenticated(View):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        messages.error(request, "Для начало необходимо авторизоваться !")
        return redirect("auth")

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView


class DeleteTask3(LoginRequiredMixin, DeleteView):
    pass

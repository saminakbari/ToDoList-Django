from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import View

from ToDoListApp.models import ToDoList


class DeleteList(LoginRequiredMixin, View):
    def get(self, request, list_id, username):
        to_do_list = ToDoList.objects.get(pk=list_id)
        to_do_list.delete()
        user = User.objects.get(username=username)
        return render(request, "v2_show_all_lists_template.html",
                      {"to_do_lists": user.to_do_lists.all(), "username": username,
                       "message": "List deleted successfully."})

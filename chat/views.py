from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *


class BaseGroupMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["groups"] = GroupChat.objects.all()
        context["current_group_id"] = getattr(self.object, "id", None)
        return context

class ChatGroupDetailView(LoginRequiredMixin, BaseGroupMixin, DetailView):
    model = GroupChat
    template_name = "group_detail.html"
    context_object_name = "group"

class ChatGroupCreateView(LoginRequiredMixin, BaseGroupMixin, CreateView):
    model = GroupChat
    fields = ["name", "description", "icon"]
    template_name = "group_create.html"

    def form_valid(self, form):
        group = form.save()
        group.members.add(self.request.user)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("group_detail", kwargs={"pk": self.object.pk})

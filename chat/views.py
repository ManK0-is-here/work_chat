from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, DetailView, ListView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST


class BaseGroupMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        my_groups = GroupChat.objects.filter(members=self.request.user)
        
        q = (self.request.GET.get("q") or "").strip()
        context["search_query"] = q
        context["search_too_short"] = False
        context["search_results"] = None

        if q:
            if len(q) < 3:
                context["search_too_short"] = True
            else:
                context["search_results"] = (
                    GroupChat.objects
                    .exclude(members=self.request.user)
                    .filter(name__icontains=q)[:20]
                )

        context["groups"] = my_groups
        context["current_group_id"] = getattr(self.object, "id", None)
        return context


class ChatGroupDetailView(LoginRequiredMixin, BaseGroupMixin, DetailView):
    model = GroupChat
    template_name = "group_detail.html"
    context_object_name = "group"

    def get_queryset(self):
        return GroupChat.objects.filter(members=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        group = self.get_object()
        context["messages"] = group.messages.select_related("sender").all()[:50]  # последние 50 сообщений
        return context

class ChatGroupCreateView(LoginRequiredMixin, CreateView):
    model = GroupChat
    fields = ["name", "description", "icon"]
    template_name = "group_create.html"

    def form_valid(self, form):
        form.instance.creator = self.request.user
        responce = super().form_valid(form)
        self.object.members.add(self.request.user)
        return responce
    
    def get_success_url(self):
        return reverse_lazy("group_detail", kwargs={"pk": self.object.pk})


class GroupChatUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = GroupChat
    fields = ["name", "description", "icon"]
    template_name = "group_edit.html"

    def test_func(self):
        return self.request.user == self.get_object().creator

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["group"] = self.get_object()
        return context

    def form_valid(self, form):
        messages.success(self.request, "Группа успешно обновлена!")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("group_detail", kwargs={"pk": self.object.pk})


def add_by_username(request, pk):
    if request.method == "POST":
        username = request.POST.get("username")
        user_to_add = User.objects.filter(username=username).first()
        group = get_object_or_404(GroupChat, pk=pk)

        if request.user != group.creator:
            messages.error(request, "Только создатель может добавлять участников!")
            return redirect("group_detail", pk=pk)

        if user_to_add:
            group.members.add(user_to_add)
            messages.success(request, f"{username} добавлен в группу!")
        else:
            messages.error(request, "Пользователь не найден")

    return redirect("group_detail", pk=pk)


def leave_group(request, pk):
    group = get_object_or_404(GroupChat, pk=pk)
    group.members.remove(request.user)
    return redirect("group_list")


@require_POST
@login_required
def join_group(request, pk):
    group = get_object_or_404(GroupChat, pk=pk)
    if not group.members.filter(id=request.user.id).exists():
        group.members.add(request.user)
        messages.success(request, f"Поздровляю, вы вступили в группу {group.name}.")
    else:
        messages.info(request, "Вы уже состоите в этой группе.")
    return redirect("group_detail", pk=group.pk)


class  GroupChatDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = GroupChat
    template_name = "group_delete.html"
    success_url = reverse_lazy("group_list")

    def test_func(self):
        return self.request.user == self.get_object().creator
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        confirm_name = request.POST.get("confirm_name")

        if confirm_name != self.object.name:
            messages.error(request, "Название группы введено неверно!")
            return redirect("group_delete", pk=self.object.pk)

        messages.success(request, f"Группа «{self.object.name}» успешно удалена!")
        return super().delete(request, *args, **kwargs)


class GroupChatListView(LoginRequiredMixin, ListView):
    model = GroupChat
    template_name = "base_groups.html"
    context_object_name = "groups"

    def get_queryset(self):
        query = self.request.GET.get("q")
        qs = GroupChat.objects.filter(members=self.request.user)

        if query:
            qs = qs.filter(name__icontains=query.strip())
        return qs


class ChatView(LoginRequiredMixin, BaseGroupMixin, DetailView):
    model = GroupChat
    template_name = "group_chat.html"
    context_object_name = "group"

    def get_queryset(self):
        return GroupChat.objects.filter(members=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        group = self.get_object()
        context["messages"] = group.messages.select_related("sender").all().order_by('timestamp')[:50]
        return context


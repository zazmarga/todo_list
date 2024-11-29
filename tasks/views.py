from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from tasks.forms import TaskCreationForm
from tasks.models import Task, Tag


class TagListView(generic.ListView):
    model = Tag
    queryset = Tag.objects.all()


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tasks:tag-list")
    template_name = "tasks/tag_form.html"


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    template_name = "tasks/tag_form.html"

    def get_success_url(self):
        return reverse_lazy("tasks:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "tasks/tag_delete.html"
    success_url = reverse_lazy("tasks:tag-list")


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.all().prefetch_related("tags")


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskCreationForm
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy("tasks:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskCreationForm
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy("tasks:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "tasks/task_delete.html"
    success_url = reverse_lazy("tasks:task-list")


class TaskSwitchDoneView(generic.UpdateView):
    model = Task
    fields = []
    template_name = "tasks/task_list.html"

    def get(self, request, *args, **kwargs):
        task = self.get_object()
        task.done = not task.done
        task.save()
        return redirect("tasks:task-list")

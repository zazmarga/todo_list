from django import forms

from .models import Task, Tag


class TaskCreationForm(forms.ModelForm):
    content = forms.CharField(
        required=True,
        label="",
        widget=forms.Textarea(
            attrs={
                "cols": "80",
                "rows": "2",
                "placeholder": "Write new task here...",
                "class": "form-control",
            }
        )
    )
    finish_time = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(
            attrs={
                "type": "datetime-local",
                "placeholder": "YYYY-MM-DD HH:MM",
                "class": "form-control form-control-sm",
            }
        ),
        label="Deadline: Date and time of finish",
    )

    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        required=True,
        widget=forms.CheckboxSelectMultiple(
            attrs={
                "class": "form-control-check"
            }
        ),
    )

    class Meta:
        model = Task
        fields = ["content", "finish_time", "tags"]

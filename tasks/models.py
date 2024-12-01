from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=63)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["name", ],
                                    name="unique_tag_name"
                                    ),
        ]
        ordering = ["name"]

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    finish_time = models.DateTimeField(blank=True, null=True)
    done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="tasks")

    class Meta:
        ordering = ["done", "-created_time"]

    def __str__(self):
        return self.content

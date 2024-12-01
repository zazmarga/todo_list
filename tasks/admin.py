from django.contrib import admin

from tasks.models import Tag, Task

admin.site.register(Tag)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("done", "content", "finish_time", "get_tags", "created_time", )
    search_fields = ("content",)
    list_filter = ("done", )

    def get_tags(self, obj):
        return ", ".join(
            [tag.name for tag in obj.tags.all()]
        )

    get_tags.short_description = "Tags"

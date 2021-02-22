from django.contrib import admin
from .models import Post, Comment, Tag
from django.utils.safestring import mark_safe

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'region', 'updated']
    list_display_links = ['id', 'title']
    ordering = ['updated']
    list_filter = ['region']
    search_fields = ['title','body']
    # list_per_page = 3

admin.site.register(Post, PostAdmin)


def make_deleted(modeladmin, request, queryset):
    queryset.update(deleted=True)
    print(type(request))
    print(type(queryset))

make_deleted.short_description = '선택된 comments를 삭제상태로 설정합니다.'



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'author', 'message_length', 'deleted']
    fields = ['post', 'author', 'message']
    actions = [make_deleted]

    def message_length(self, obj):
        return len(obj.message)

    message_length.short_description = '댓글 글자수'


admin.site.register(Tag)


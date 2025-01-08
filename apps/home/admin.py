from django.contrib import admin

from . import models


class GenreAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']


class GameImageInline(admin.StackedInline):
    model = models.GameImage
    extra = 1
    max_num = 3


class GameAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'downloads', 'size', 'genre', 'added_at']
    list_display_links = ['id', 'name']
    list_editable = ['genre']
    list_filter = ['genre', 'added_at']
    inlines = [
        GameImageInline
    ]


class LibraryItemInline(admin.TabularInline):
    model = models.LibraryItem
    extra = 1


class LibraryAdmin(admin.ModelAdmin):
    inlines = [LibraryItemInline]


admin.site.register(models.Library, LibraryAdmin)
admin.site.register(models.Genre, GenreAdmin)
admin.site.register(models.Stream)
admin.site.register(models.Game, GameAdmin)
admin.site.register(models.UserClip)

from django.contrib import admin
from .models import *

class MediaFileInline(admin.TabularInline):
    model = MediaFile
    extra = 0


class MediaFileFileAdmin(admin.ModelAdmin):
    list_display = [field.name for field in MediaFile._meta.fields]

    class Meta:
        model = MediaFile

admin.site.register(MediaFile, MediaFileFileAdmin)


# Register your models here.

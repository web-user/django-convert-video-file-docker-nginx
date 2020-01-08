import os, sys, inspect
import ffmpy
import time
from django.db import models
from convertfile.utils import unique_slug_generator, get_filename, get_size_filename, validate_file_extension
from django.db.models.signals import pre_save, post_save, m2m_changed, pre_delete


def execution_path(filename):
    frame = sys._getframe(1)
    if hasattr(frame, "_frame"):
        frame = frame._frame
    return os.path.join(os.path.dirname(inspect.getfile(frame)), filename)


def upload_media_file(instance, filename):
    location = "media-file/"
    return location + filename  #"path/to/filename.mp4"


class MediaFile(models.Model):
    file    = models.FileField(upload_to=upload_media_file, validators=[validate_file_extension], default='')
    objects = models.Manager()

    def __str__(self):
        return str(self.file.name)


    @property
    def filesize(self):
        return round(self.file.size/1000000, 2)

    def save(self, *args, **kwargs):
        # Check how the current values differ from ._loaded_values. For example,
        # prevent changing the creator_id of the model. (This example doesn't
        # support cases where 'creator_id' is deferred).
        super().save(*args, **kwargs)


def file_pre_save_receiver(sender, instance, *args, **kwargs):
    instance.file.name = unique_slug_generator(instance)

pre_save.connect(file_pre_save_receiver, sender=MediaFile)


def file_post_save_receiver(sender, instance, created, **kwargs):
    if instance.filesize > 2.5 and os.path.splitext(instance.file.path)[1] == '.mp4':

        ff = ffmpy.FFmpeg(
            inputs={instance.file.path: None},
            outputs={os.path.splitext(instance.file.path)[0] + '.gif': None})
        ff.run()
        time.sleep(3)
        os.remove(instance.file.path)
        MediaFile.objects.filter(file=instance).update(file=os.path.splitext(instance.file.path)[0] + '.gif')


post_save.connect(file_post_save_receiver, sender=MediaFile)


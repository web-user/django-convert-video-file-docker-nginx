import datetime
import os
import random
import string

from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.text import slugify

from convertfile.settings import BASE_DIR


def get_filename(path): #/abc/filename.mp4
    return os.path.basename(path)


def get_size_filename(path): #/abc/filename.mp4
    print(get_filename)
    print(os.path.join(os.path.dirname(BASE_DIR), 'media'))
    # statinfo = os.stat("{}/{}".format(os.path.join(os.path.dirname(BASE_DIR), 'media'), path))
    return statinfo.st_size


def validate_file_extension(value):
    print("MY PATH - ", value.path)

    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf', '.doc', '.docx', '.jpg', '.png', '.xlsx', '.xls', '.mp4', '.gif']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Unsupported file extension. Supported .pdf, .doc, .docx, .jpg, .png, .xlsx, .xls, .mp4, .gif')

def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def unique_slug_generator(instance, new_file=None):
    """
    This is for a Django project and it assumes your instance
    has a model with a slug field and a title character (char) field.
    """
    filename = os.path.splitext(instance.file.name)[0]
    fileext = os.path.splitext(instance.file.name)[1]
    if new_file is not None:
        file = new_file
    else:
        file = "{}{}".format(slugify(filename),fileext)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(file=file).exists()
    if qs_exists:
        new_file = "{randstr}-{file}".format(
                    file=file,
                    randstr=random_string_generator(size=4)
                )
        return unique_slug_generator(instance, new_file=new_file)
    return file

from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Book

@receiver(post_save, sender=Book)
def create_thumbnail(sender, instance, created, **kwargs):
    if not instance.image or instance.thumbnail:
        return
    img = Image.open(instance.image)
    img.thumbnail((200, 200))
    buffer = BytesIO()
    img_format = img.format or 'JPEG'
    img.save(buffer, format=img_format)
    file_name = instance.image.name.split('/')[-1]
    instance.thumbnail.save(file_name, ContentFile(buffer.getvalue()), save=False)
    Book.objects.filter(pk=instance.pk).update(thumbnail=instance.thumbnail)
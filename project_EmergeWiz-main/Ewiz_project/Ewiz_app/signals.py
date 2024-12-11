from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import JobOpenings

@receiver(post_delete, sender=JobOpenings)
def delete_image_file(sender, instance, **kwargs):
    if instance.logo:  # Replace 'image' with your field name
        instance.logo.delete(save=False)
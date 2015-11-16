from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver
from django.conf import settings
from fredslist.models import Post
from django.core.mail import send_mail


@receiver(post_save, sender=Post)
def post_post_save(sender, **kwargs):
    print("a post was saved and an email was sent")
    send_mail("New Post in Fredslist", "A new post was just created in fredslist", "Cesar Marroquin <cesarm2333@gmail.com>",
              ["cesarwebdevelopment@gmail.com"])

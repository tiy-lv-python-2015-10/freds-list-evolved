from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from peteslist.models import Post, Keyword


@receiver(post_save, sender=User)
def create_user_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


@receiver(post_save, sender=Post)
def send_alert(sender, instance=None, created=False, **kwargs):
    if created:
        for user in User.objects.all():
            keywords = user.keyword_set.all()
            for keyword in keywords:
                low_key = keyword.keyword.lower()
                if low_key in instance.title.lower() or low_key in \
                        instance.description.lower():
                    Keyword.objects.create(user=user, keyword='BINGO')

                    # mail = EmailMultiAlternatives(
                    #     subject="New Post with your keyword!",
                    #     body="A new post has been created. We are sending you "
                    #          "this email to inform you that it contains a "
                    #          "keyword that you have in your account settings.",
                    #     from_email="Peter Flynn <fredoflynn@gmail.com>",
                    #     to=['palfredo119@hotmail.com',],
                    #     headers={"Reply-to": "support@mysite.com"}
                    # )
                    # mail.attach_alternative("<h2>Peteslist alert</h2>"
                    #                         "<p>Cool I can put HTML here.</p>",
                    #                          "text/html")
                    # mail.send()
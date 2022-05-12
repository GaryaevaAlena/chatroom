from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):

    CHOICES = (('male', 'Мужской пол'), ('female', 'Женский пол'))

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='uploads/', blank=True)
    sex = models.CharField(max_length=10, choices=CHOICES, default='male', verbose_name=("Пол"))

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return f'{self.user.username}'

class Chat(models.Model):

    penPal = models.ManyToManyField(User)
    nameChat = models.CharField(max_length=30, verbose_name=("Название чата"))

    def __str__(self):
        return f'{self.nameChat}'

    def get_absolute_url(self):
        return f'/page/{self.id}/'
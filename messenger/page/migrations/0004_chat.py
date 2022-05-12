# Generated by Django 4.0.4 on 2022-05-05 07:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('page', '0003_remove_profile_birthday_alter_profile_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameChat', models.CharField(max_length=30)),
                ('penPal', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
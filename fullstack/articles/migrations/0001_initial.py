# Generated by Django 4.2.2 on 2023-06-25 21:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('channels', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=100)),
                ('article_description', models.TextField()),
                ('article_created_date', models.DateField(auto_now_add=True)),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='channels.channel')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_articles', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

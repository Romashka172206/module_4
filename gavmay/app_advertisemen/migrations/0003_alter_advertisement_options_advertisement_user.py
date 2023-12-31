# Generated by Django 4.2.3 on 2023-08-09 16:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_advertisemen', '0002_alter_advertisement_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='advertisement',
            options={'verbose_name': 'Объявление', 'verbose_name_plural': 'Объявления'},
        ),
        migrations.AddField(
            model_name='advertisement',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь'),
            preserve_default=False,
        ),
    ]

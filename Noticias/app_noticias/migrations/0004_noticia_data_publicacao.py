# Generated by Django 3.0.3 on 2020-02-29 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_noticias', '0003_noticia_auto'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='data_publicacao',
            field=models.DateField(blank=True, max_length=128, null=True, verbose_name='data publicação'),
        ),
    ]

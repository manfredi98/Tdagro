# Generated by Django 3.2.9 on 2021-11-02 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Agrodigital', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='encuesta',
            name='dimension1',
            field=models.CharField(choices=[('1', 'muy malo'), ('2', 'malo'), ('3', 'intermedio')], default=0.0004948045522018803, max_length=1, verbose_name='dimension1'),
            preserve_default=False,
        ),
    ]

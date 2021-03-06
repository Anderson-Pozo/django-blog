# Generated by Django 2.2.6 on 2019-11-16 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0005_auto_20191116_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='facebook',
            field=models.URLField(blank=True, default='#', null=True, verbose_name='Facebook'),
        ),
        migrations.AlterField(
            model_name='autor',
            name='github',
            field=models.URLField(blank=True, default='#', null=True, verbose_name='GitHub'),
        ),
        migrations.AlterField(
            model_name='autor',
            name='twitter',
            field=models.URLField(blank=True, default='#', null=True, verbose_name='Twitter'),
        ),
        migrations.AlterField(
            model_name='autor',
            name='web',
            field=models.URLField(blank=True, default='#', null=True, verbose_name='Web'),
        ),
    ]

# Generated by Django 2.0.5 on 2018-06-14 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hansard', '0004_auto_20180614_0315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='debatereference',
            name='debate_title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='debatereference',
            name='subdebate1_title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='debatereference',
            name='subdebate2_title',
            field=models.CharField(max_length=255),
        ),
    ]

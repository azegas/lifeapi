# Generated by Django 4.2.2 on 2023-06-27 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='type',
            field=models.CharField(choices=[('YN', 'Yes/No'), ('Scale', 'Scale 1-5'), ('Text', 'Text')], default='Text', max_length=10),
        ),
    ]

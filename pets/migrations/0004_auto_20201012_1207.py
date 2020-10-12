# Generated by Django 3.1.2 on 2020-10-12 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0003_auto_20201012_1109'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='test',
            field=models.CharField(default=0, max_length=2),
        ),
        migrations.AlterField(
            model_name='pet',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='pet',
            name='type',
            field=models.CharField(choices=[('dog', 'Dog'), ('cat', 'Cat'), ('parrot', 'Parrot'), ('unknown', 'Unknown')], default='unknown', max_length=7),
        ),
    ]

# Generated by Django 4.2.5 on 2023-09-13 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commande', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='commande',
            options={'ordering': ('-created_at',)},
        ),
        migrations.AlterField(
            model_name='commande',
            name='status',
            field=models.CharField(choices=[('ordered', 'ordered'), ('shipped', 'shipped')], default='ordered', max_length=30),
        ),
    ]

# Generated by Django 3.1.4 on 2020-12-10 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20201210_1203'),
    ]

    operations = [
        migrations.AddField(
            model_name='commande',
            name='plat',
            field=models.ManyToManyField(to='blog.Plat'),
        ),
        migrations.AlterField(
            model_name='commande',
            name='status',
            field=models.CharField(choices=[('Livre', 'Livré'), ('Attente', 'En Attente')], max_length=20),
        ),
    ]